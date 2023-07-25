# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all the contents of the current directory into the container
COPY . .

# Install the required dependencies
RUN pip install --upgrade pip -r requirements.txt

 
# Expose the port that FastAPI will be running on (replace 8000 with your desired port)
EXPOSE 8000

# Set the command to run your FastAPI app using uvicorn (replace your_fastapi_app.main:app with your app's entry point)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]