import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is missing from .env")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load JSON: {e}")
        sys.exit(1)

def ask_openai(data_text, question=None):
    prompt = f"This is a JSON file:\n\n{data_text}"
    if question:
        prompt += f"\n\nNow answer this question: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional data engineer."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py path/to/file.json")
        sys.exit(1)

    filepath = sys.argv[1]
    data = load_json(filepath)
    json_excerpt = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(ask_openai(json_excerpt))

    if input("\nWould you like to ask a follow-up question? (y/n): ").strip().lower() == "y":
        user_question = input("Your question: ")
        print("\n--- AI Answer ---")
        print(ask_openai(json_excerpt, user_question))

if __name__ == "__main__":
    main()
