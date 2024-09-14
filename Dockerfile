# Use an official Python runtime as a parent image
FROM python:3.11.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app/mt5lt

# Copy the current directory contents into the container at /app
COPY . /app/mt5lt  
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]