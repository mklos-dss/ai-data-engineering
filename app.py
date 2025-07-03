import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API key securely
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is missing in your .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not load JSON file: {e}")
        sys.exit(1)

def generate_insight(content, question=None):
    prompt = f"Analyze this JSON data:\n\n{content}"
    if question:
        prompt += f"\n\nFollow-up question: {question}"

    try:
        reply = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a skilled data analyst. Provide clear, useful insights."},
                {"role": "user", "content": prompt}
            ]
        )
        return reply.choices[0].message.content
    except Exception as e:
        print(f"[OpenAI API ERROR] {e}")
        sys.exit(1)

def run():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_json>")
        sys.exit(1)

    filepath = sys.argv[1]
    data = load_json_file(filepath)
    sample = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(generate_insight(sample))

    ask = input("\nAsk a follow-up question? (y/n): ").strip().lower()
    if ask == "y":
        q = input("Your question: ")
        print("\n--- AI Answer ---")
        print(generate_insight(sample, q))

if __name__ == "__main__":
    run()
