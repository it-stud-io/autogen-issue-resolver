# README SVC2
This service is the second service in chain.
It calls service 1 to return a random number between 1 and 500 and adds 50 to it.
If the number equals 350 the service raises an exception.

The service runs on python:3.13.1-slim-bookworm and exposes port 5002.
Following endpoints are available:
- /data: GET > calls svc1/data to get the random number adds 50 to it
- /health: GET > returns the health status of the service
- /logs: GET > returns all logs of the service (used by observer agents)
- /viewlogs1: GET > returns last 15 lines logs of the service (used by VueJS frontend)

[BACK](../README.md)