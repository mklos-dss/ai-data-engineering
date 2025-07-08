import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        sys.exit(1)

def call_gpt(text, question=None):
    prompt = f"The following is a JSON file:\n\n{text}"
    if question:
        prompt += f"\n\nNow answer this question: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a skilled data analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py path/to/file.json")
        sys.exit(1)

    path = sys.argv[1]
    data = load_json(path)
    snippet = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(call_gpt(snippet))

    if input("\nWould you like to ask a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Your question: ")
        print("\n--- AI Answer ---")
        print(call_gpt(snippet, question))

if __name__ == "__main__":
    main()
