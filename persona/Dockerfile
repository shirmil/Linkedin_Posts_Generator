# Step 1: Specify a Base Image
FROM python:3.10-slim

# Step 2: Set the Working Directory in the Container
WORKDIR /app

# Step 3: Copy the Local Files to the Container
COPY . /app

# Step 4: Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

# Step 5: Specify the Command to Run the Application
CMD ["python", "main_persona.py"]