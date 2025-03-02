# README AGTS
This server runs 1 issue resolver agent and 3 service observer agents (per service).
All observer agents are able to check service health status and logs by calling the /health and /logs endpoints of the services.

The agt.py file needs your OpenAI API key to run the agents with the gpt-4o model.

The service runs on python:3.13.1-slim-bookworm and exposes port 5003.
Following endpoints are available:
- /investigate: GET > this starts the AutoGen Assistant Agent swarm
- /agentlogs: GET > returns all logs of the agent service to diplay in the VueJS frontend
- /conclusion: GET > returns the final conclusion of the issue resolver agent (used by VueJS frontend)

[BACK](../README.md)