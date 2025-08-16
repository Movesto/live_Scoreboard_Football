FROM python:3.11-slim

# Set the working directory inside the container.
# All subsequent commands will run from this path.
WORKDIR /app

# Copy the requirements file into the container first.
# This is a best practice that takes advantage of Docker's layer caching.
COPY requirements.txt .

# Install the Python dependencies defined in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container.
COPY . .

# Tell Docker that the container will listen on port 5000 at runtime.
EXPOSE 5000

# The command to run when the container starts.
# This executes your Flask application.
CMD ["python", "app.py"]