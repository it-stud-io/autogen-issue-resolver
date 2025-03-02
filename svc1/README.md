# README SVC1
This service is the first service in chain.
It generates a random number between 1 and 500 and sends it to the next service in chain.
If the number equals 250 the service raises an exception.

The service runs on python:3.13.1-slim-bookworm and exposes port 5001.
Following endpoints are available:
- /data: GET > returns a random number between 1 and 500
- /health: GET > returns the health status of the service
- /logs: GET > returns all logs of the service (used by observer agents)
- /viewlogs1: GET > returns last 15 lines logs of the service (used by VueJS frontend)

[BACK](../README.md)