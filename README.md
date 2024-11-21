# Posts Generator

## Overview
Posts Generator is a project designed to fetch articles from various sources, filter them using OpenAI's GPT-3.5-turbo model, and generate professional LinkedIn posts based on the articles and user profile information. The project uses Docker Compose to manage multiple services, including fetching articles, generating posts, and managing user profiles.

## Features
- Define a personal profile 
- Fetch articles from Google News and other specified websites.
- Generate professional LinkedIn posts based on articles and user profile information using OpenAI's GPT-3.5-turbo model
- Store generated posts in a JSON file for easy access and management.

## Project Structure

      Posts_Generator/ 
         ├── data/ 
         │  ├── articles.json
         │  ├── posts.json
         │  └── profile.json 
         ├── persona/
         │  ├── Dockerfile
         │  └── main_persona.py 
         ├── web/
         │  ├── Dockerfile
         │  └── main_web.py 
         ├── generator/
         │  ├── Dockerfile
         │  └── main_generator.py 
         ├── docker-compose.yml 
         └── README.md


## Getting Started

### Prerequisites
- Docker
- Docker Compose
- OpenAI API Key

### Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/Posts_Generator.git
   cd Posts_Generator

2. **Set Up Environment Variables Create a `.env` file in the root directory and add your OpenAI API key:**
   ```sh
   OPENAI_API_KEY=your_openai_api_key

3. **Build and Run the Services Use Docker Compose to build and run the services:**
   ```sh
   docker-compose up --build

### Services

* **Persona Service**

  The persona service manages user profiles. It collects user information and stores it in profile.json.

* **Web Service**
  
  The web service fetches articles from Google News and other specified websites and stores the filtered articles in articles.json.

* **Generator Service**
  
  The generator service reads articles from articles.json, generates professional LinkedIn posts using OpenAI's GPT-3.5-turbo model and user profile information from profile.json, and stores the generated posts in posts.json.


### Usage

1. **Run the Persona Service**
   ```sh
   docker-compose run --rm persona
3. **Run the Web Service**
   ```sh
   docker-compose run --rm web
5. **Run the Generator Service**
   ```sh
   docker-compose run --rm generator

**Example Profile**

Here is an example of what the `profile.json` file might look like after using the persona service:

      {
          "name": "John Doe",
          "job_title": "Software Engineer",
          "interests": "Technology, AI, Machine Learning",
          "tone": "professional",
          "audience": "professionals"
      }

**Example Articles**

Here is an example of what the `articles.json` file might look like after using the web service:

       {
           "title": "Latest Advances in AI",
           "link": "http://example.com/ai",
           "summary": "This article discusses the latest advances in AI.",
           "interest": "AI"
       }
    
**Example Posts**

Here is an example of what the `posts.json` file might look like:

       {
           "content": "Check out this article about AI: This article discusses the latest advances in AI. Read more here: http://example.com/ai",
           "interest": "AI",
           "link": "http://example.com/ai"
       }
    
## Contributing ##
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

