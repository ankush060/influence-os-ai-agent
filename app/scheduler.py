import json
import time
from datetime import datetime
import os

def load_scheduled_posts():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "..", "data", "scheduled_posts.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def simulate_posting(posts):
    print("🔁 Starting content scheduler...\n")
    while posts:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[DEBUG] Checking at {now}...")


        for post in posts[:]:
            print(f"[DEBUG] Scheduled for {post['post_time']}") 
            
            
            if post["post_time"] <= now:
                print(f"\n🕒 Posted at {now}:\n{post['content']}\n")
                posts.remove(post)
        time.sleep(10)  # check every 10 seconds

if __name__ == "__main__":
    posts = load_scheduled_posts()
    simulate_posting(posts)
