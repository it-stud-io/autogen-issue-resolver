# README SVC3
This service is the third service in chain.
It calls service 2 every 1 second to retrieve a random / calculated number.

The service runs on python:3.13.1-slim-bookworm and exposes port 5003.
Following endpoints are available:
- /start: GET > calls svc2/data to get the random / calculated number every 1 second > this starts the service chain
- /health: GET > returns the health status of the service
- /logs: GET > returns all logs of the service (used by observer agents)
- /viewlogs1: GET > returns last 15 lines logs of the service (used by VueJS frontend)

[BACK](../README.md)