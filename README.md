# autogen-issue-resolver

## AutoGen Issue Resolver Prototype
This is a simple prototyp using AutoGen Multi-Agent framework to resolve issues in a distributed system.

## How to run
To use the AutoGen Assistant Agents on OpenAI GPT-4o you need to have an OpenAI account and API key and need to set it in the file [agts/agent.py](./agts/agt.py).

This prototype needs docker and docker-compose to run. To start the system, run the following command in the root directory of the project:

```bash
docker-compose up
```

This will start the system with 5 containers:

1. Service 1 (Python Flask App, svc1) - generating a random number between 1 and 500 [README](./svc1/README.md)
2. Service 2 (Python Flask App, svc2) - requesting the random number from Service 1 and adding 50 [README](./svc2/README.md)
3. Service 3 (Python Flask App, svc3) - requesting the calculated number from Service 2 [README](./svc3/README.md)
4. A 4th Python Flask App (agts) running 4 AutoGen Assistant Agents (1 Issue Resolver & 3 Service Observer) - investigating issues in the system [README](./agts/README.md)
5. A VueJS frontend (frontend) to visualize the system state and AutoGen agent results [README](./web/README.md)

After the system is started, you can access the frontend at http://localhost:8080.