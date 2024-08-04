# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Update package lists and install OpenGL libraries
RUN apt-get update && apt-get install -y \
        libgl1-mesa-glx \   
        libglib2.0-0     

# Environment variables
ENV DISPLAY=:0

# Copy the project files into the container
COPY . .

# Set the entry point for the container
CMD [ "python", "main.py" ]
