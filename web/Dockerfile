# Step 1: Specify a Base Image
FROM python:3.10-slim

# Step 2: Set the Working Directory in the Container
WORKDIR /app

# Step 3: Copy the Local Files to the Container
COPY . /app

# Step 3.1: Copy the wait-for-it.sh script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Step 4: Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
ENV OPENAI_API_KEY='Enter your OpenAI API Key here'
ENV GOOGLE_CUSTOM_SEARCH_API_KEY='AIzaSyAY1vjGeft8jREpabgTeIX9A-R5kqHFXjg'
ENV GOOGLE_CUSTOM_SEARCH_ENGINE_ID='a198f8824f3664045'
ENV NUMBER_OF_ARTICLES=5

# Step 5: Specify the Command to Run the Application
CMD ["python", "main_web.py"]