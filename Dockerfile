# Use official Python image
FROM python:alpine

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations and start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
