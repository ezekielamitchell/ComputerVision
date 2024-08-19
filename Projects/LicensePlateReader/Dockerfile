# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir opencv-python numpy matplotlib

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME LicensePlateReader

# Run main.py when the container launches
CMD ["python3", "main.py"]
