# Use the official Python image from the DockerHub
FROM python:3.13.1-slim-bookworm

# Set the working directory in docker
WORKDIR /svc3

# Copy the dependencies file to the working directory
# COPY requirements.txt .
COPY pyproject.toml .
# COPY README.md .
# COPY startup.sh .

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install .

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "svc.py"]