# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port your app will run on
EXPOSE 5000

# Define the command to run your app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
