from flask import Flask, jsonify
import logging
import requests

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import HandoffTermination, TextMentionTermination
from autogen_agentchat.messages import HandoffMessage
from autogen_agentchat.teams import Swarm
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

logging.basicConfig(filename='agt.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

conclusion = None

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key="sk-proj-xxx", # SET YOUR OPENAI API KEY HERE
)

def get_health_status(url: str) -> str:
    """calling health status endpoint"""
    return requests.get(url)

def get_logs(url: str) -> str:
    """calling service logs endpoint"""
    return requests.get(url)

def get_svc1_health_status() -> str:
    """get service 1 health status"""
    return get_health_status('http://svc1:5001/health')

def get_svc1_logs() -> str:
    """get service 1 logs"""
    return get_logs('http://svc1:5001/logs')

def get_svc2_health_status() -> str:
    """get service 2 health status"""
    return get_health_status('http://svc2:5002/health')

def get_svc2_logs() -> str:
    """get service 2 logs"""
    return get_logs('http://svc2:5002/logs')

def get_svc3_health_status() -> str:
    """get service 3 health status"""
    return get_health_status('http://svc3:5003/health')

def get_svc3_logs() -> str: 
    """get service 3 logs"""
    return get_logs('http://svc3:5003/logs')


svc1_observer = AssistantAgent(
    "svc1_observer",
    model_client=model_client,
    handoffs=["issue_resolver"],
    tools=[get_svc1_health_status, get_svc1_logs],
    system_message="""You are a service observer agent.
    The service observer is in charge of get service health status and logs and return to the issue resolver.
    When the transaction is complete, handoff to the issue resolver to finalize.""",
)

svc2_observer = AssistantAgent(
    "svc2_observer",
    model_client=model_client,
    handoffs=["issue_resolver"],
    tools=[get_svc2_health_status, get_svc2_logs],
    system_message="""You are a service observer agent.
    The service observer is in charge of get service health status and logs and return to the issue resolver.
    When the transaction is complete, handoff to the issue resolver to finalize.""",
)

svc3_observer = AssistantAgent(
    "svc3_observer",
    model_client=model_client,
    handoffs=["issue_resolver"],
    tools=[get_svc3_health_status, get_svc3_logs],
    system_message="""You are a service observer agent.
    The service observer is in charge of get service health status and logs and return to the issue resolver.
    When the transaction is complete, handoff to the issue resolver to finalize.""",
)

issue_resolver = AssistantAgent(
    "issue_resolver",
    model_client=model_client,
    handoffs=["svc1_observer", "svc2_observer", "svc3_observer"],
    system_message="""You are an agent specialized in investigating and resolving issues.
    You have the ability to reach out to service observers to investigate which service caused an issue.
    When the investigation is complete use TERMINATE to end the transaction.""",
)

termination = TextMentionTermination("TERMINATE")
team = Swarm([issue_resolver, svc1_observer, svc2_observer, svc3_observer], termination_condition=termination)

task = "Investigate which service has threw an error and why."

async def run_team_stream() -> None:
    global conclusion
    task_result = await Console(team.run_stream(task=task))
    logging.info(f"TASK RESULT: {task_result}")
    last_message = task_result.messages[-1]
    logging.info(f"LAST MESSAGE: {last_message}")
    conclusion = last_message.content

@app.route('/investigate')
async def investigate():
    result = await run_team_stream()
    logging.info(f"INVESTIGATION STARTED: {result}")
    return jsonify({"message": "Investigation started."})

@app.route('/agentlogs')
def agentlogs():
    with open('agt.log', 'r') as f:
        return f.read()
    
@app.route('/conclusion')
def conclusion():
    global conclusion
    return jsonify({"conclusion": conclusion})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5004)
    logging.info(f"Server listening on localhost:5004")