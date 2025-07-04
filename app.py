import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: Missing OPENAI_API_KEY in your .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        sys.exit(1)

def ask_openai(content, followup=None):
    prompt = f"Analyze and describe this mining-related JSON:\n\n{content}"
    if followup:
        prompt += f"\n\nUser follow-up: {followup}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data analyst specializing in mining and industrial operations."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as err:
        print(f"OpenAI API Error: {err}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    data = load_json(filepath)
    text = json.dumps(data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(ask_openai(text))

    if input("\nAsk a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Your question: ")
        print("\n--- AI Answer ---")
        print(ask_openai(text, question))

if __name__ == "__main__":
    main()
