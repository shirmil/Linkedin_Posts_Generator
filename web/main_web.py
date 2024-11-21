import json
import requests
from bs4 import BeautifulSoup
import os
# docker build -t web_image . 
# docker run -it --rm -v $(pwd)/../data:/app/data web_image

profile_path = os.getenv("PROFILE_PATH")
articles_path = os.getenv("ARTICLES_PATH")

def load_profile():
    profile_path = "/app/data/profile.json"
    with open(profile_path, "r") as f:
        profile = json.load(f)
    return profile["interests"]

def fetch_google_news(query):
    url = f"https://news.google.com/search?q={query}&hl=en-US&when:2d"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.select("article"):
        headline = item.select_one("h3").text if item.select_one("h3") else "No title"
        link = "https://news.google.com" + item.find("a", href=True)["href"][1:]
        articles.append({"title": headline, "link": link})

    return articles

def main():

    # load profile
    interests = load_profile()
    if not interests:
        print("No interests found in the profile. Exiting.")
        return
    interests = interests.split(",")

    # set jason to store articles
    all_important_articles = []
    

    for interest in interests:
        print("=====================================")
        print("Fetching top stories for:", interest.strip())
        print("=====================================")
        news = fetch_google_news(interest.strip())
        num_of_articles_per_interest = os.getenv("NUM_OF_ARTICLES", 5)
        for article in news[:num_of_articles_per_interest]:
            # add interest to article
            # article["interest"] = interest.strip()
            print(article["title"], article["link"])
            all_important_articles.append(article)

    print(all_important_articles)

    with open(articles_path, "w") as f:
        json.dump(all_important_articles, f, indent=4)


if __name__ == "__main__":
    main()