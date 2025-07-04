import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY missing in your environment.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to read JSON file: {e}")
        sys.exit(1)

def analyze_json(content, question=None):
    prompt = f"Analyze this JSON data:\n\n{content}"
    if question:
        prompt += f"\n\nUser question: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert data scientist providing clear insights."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    json_data = load_json_file(filepath)
    snippet = json.dumps(json_data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(analyze_json(snippet))

    if input("\nAsk a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Enter your question: ")
        print("\n--- AI Answer ---")
        print(analyze_json(snippet, question))

if __name__ == "__main__":
    main()
