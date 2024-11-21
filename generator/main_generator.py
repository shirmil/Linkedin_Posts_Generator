import json
import os
import openai
from openai import OpenAI

profile_path = os.getenv("PROFILE_PATH")
articles_path = os.getenv("ARTICLES_PATH")
posts_path = os.getenv("POSTS_PATH")
client = OpenAI(
 api_key=os.getenv("OPENAI_API_KEY"),
)

def load_articles():
    print("Loading articles...")
    articles_path = "../../app/data/articles.json"
    if os.path.exists(articles_path):
        with open(articles_path, "r") as f:
            articles = json.load(f)
        return articles
    else:
        print("No articles found")
        return []

def load_profile():
    print("Loading profile...")
    profile_path = "../../app/data/profile.json"
    if os.path.exists(profile_path):
        with open(profile_path, "r") as f:
            profile = json.load(f)
        return profile
    else:
        print("No profile found")
        return {}


def generate_post(article, profile):
    print("\n")
    print("Generating post...\n")
    title = article.get("title", "No Title")
    link = article.get("link", "No Link")
    summary = article.get("summary", "No Summary")
    interest = article.get("interest", "General")

    profile_name = profile.get("name", "User")
    profile_job_title = profile.get("job_title", "Professional")
    profile_interests = profile.get("interests", "various topics")

    prompt = (
        f"Create a profesional linkedin post for a {profile_job_title}."
        f"The post should be about the following article: {link}\n"
        f"and be written in a {profile.get('tone', 'professional')} tone.\n"
        f"The post should be aimed at {profile.get('audience', 'professionals')}.\n"
        f"The post should be written by {profile_name} who is a {profile_job_title}.\n"
        f"the post should start with a title.\n"
        f"return the post directly without any additional information.\n"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    post_content = response.choices[0].message.content.strip()

    post = {
        "content": post_content,
        "interest": interest,
        "link": link

    }

    print("\n ############################################################ \n")
    print(post["content"])
    print("\n ############################################################ \n")
    return post

def main():
    # Load articles
    articles = load_articles()
    if not articles:
        print("No articles to process. Exiting.")
        return

    # Load profile
    profile = load_profile()
    if not profile:
        print("No profile information found. Exiting.")
        return

    # Generate posts
    posts = []
    for article in articles:
        post = generate_post(article, profile)
        posts.append(post)

    # Save posts to a file
    try:
        print(f"Saving posts to: {posts_path}")
        with open(posts_path, "w") as f:
            json.dump(posts, f, indent=4)
        print("Posts saved to posts.json")
    except Exception as e:
        print(f"An error occurred while saving posts: {e}")

if __name__ == "__main__":
    main()