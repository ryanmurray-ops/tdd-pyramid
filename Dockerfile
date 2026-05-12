FROM python:3.12

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Indicate that the app will run on port 3000
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]