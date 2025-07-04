import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment configuration
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY not set in .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def read_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as err:
        print(f"Failed to read JSON file: {err}")
        sys.exit(1)

def query_ai(json_text, followup=None):
    prompt = f"Review and summarize this JSON:\n\n{json_text}"
    if followup:
        prompt += f"\n\nAdditional question: {followup}"

    try:
        result = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in data integration and AI analytics."},
                {"role": "user", "content": prompt}
            ]
        )
        return result.choices[0].message.content
    except Exception as e:
        print(f"API Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    json_data = read_json_file(filepath)
    json_text = json.dumps(json_data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(query_ai(json_text))

    if input("\nWould you like to ask a follow-up question? (y/n): ").strip().lower() == "y":
        user_question = input("Your question: ")
        print("\n--- AI Answer ---")
        print(query_ai(json_text, user_question))

if __name__ == "__main__":
    main()
