import requests
import os
import json

API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_content(profile_data):
    prompt = f"""
You are an AI content creator for LinkedIn personal branding.

Using the following profile data:
{json.dumps(profile_data, indent=2)}

Generate 3 types of posts for the user:
1. A short text-only post (for engagement)
2. A carousel post idea with slide titles
3. A long-form article summary

Each post should be professional, engaging, and aligned with the user's skills and interests.
Use a friendly tone. End short posts with 1-2 hashtags.
"""

    body = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {response.status_code}: {response.text}"

def load_profile():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "..", "data", "sample_profile.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    profile = load_profile()
    output = generate_content(profile)
    print("\n📝 Generated LinkedIn Content:\n")
    print(output)
