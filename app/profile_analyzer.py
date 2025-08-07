import json
import requests
import os

# STEP 1: Load your profile JSON
def load_profile():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "..", "data", "sample_profile.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# STEP 2: Send it to OpenRouter using Claude or Mixtral
def analyze_profile(profile_data):
    api_key = "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"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Analyze this LinkedIn profile and provide:
    1. A short professional summary
    2. Strengths based on skills and experience
    3. Suggested LinkedIn content topics to grow personal brand
    4. Tone or writing style suggestions
    
    Profile data:
    {json.dumps(profile_data, indent=2)}
    """

    body = {
        "model": "mistralai/mixtral-8x7b-instruct",  # You can try other models too
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body
    )

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# STEP 3: Run the script
if __name__ == "__main__":
    profile = load_profile()
    analysis = analyze_profile(profile)
    print("\n🔍 Profile Analysis:\n")
    print(analysis)
