import json
import os

# bild docker: docker build -t persona_image .
# create image: docker run -it --rm -v $(pwd)/../data:/app/data persona_image

profile_path = os.getenv("PROFILE_PATH")

def build_profile():

    # Check if a profile already exists
    if os.path.exists(profile_path):
        # print current profile
        with open(profile_path, "r") as f:
            profile = json.load(f)
            print("\nCurrent profile:")
            for key, value in profile.items():
                print(f"{key}: {value}")
        response = input("A profile already exists. Do you want to overwrite it? (y/n) ")
        if response.lower() != "y":
            print("Exiting without saving.")
            return

    # Create a new profile
    profile = {}
    
    # Ask questions to build the profile
    profile["name"] = input("Enter your name: ")
    profile["job_title"] = input("Enter your job title: ")
    profile["interests"] = input("List some professional interests: ")
    profile["posts frequancy"] = input("How often do you want to write posts (e.g., daily, weekly, monthly)? ")
    profile["audience"] = input("Who is your target audience? ")
    profile["tone"] = input("What tone do you want to convey in your writing (e.g., informative, humorous)? ")


    with open(profile_path, "w") as f:
        json.dump(profile, f)
    
    print("\nProfile saved! The generator and web services can now use this information.")
    print(f"profile.json saved to {profile_path}")

if __name__ == "__main__":
    print("main_persona is running")
    build_profile()

