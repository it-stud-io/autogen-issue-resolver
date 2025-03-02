# Use the official Node image from the DockerHub
FROM node:20-bookworm-slim

# Set the working directory in docker
WORKDIR /web

# Copy the dependencies file to the working directory
# COPY requirements.txt .
COPY package.json .
COPY README.md .

# Install any dependencies
RUN npm install

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["npm", "run", "serve"]