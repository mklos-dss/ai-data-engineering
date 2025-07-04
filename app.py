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

def read_json_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as error:
        print(f"Failed to load JSON file: {error}")
        sys.exit(1)

def generate_insights(json_text, user_question=None):
    prompt = f"Analyze this JSON data:\n\n{json_text}"
    if user_question:
        prompt += f"\n\nFollow-up question: {user_question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable AI data analyst providing actionable insights."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as err:
        print(f"OpenAI API error: {err}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    json_data = read_json_file(file_path)
    snippet = json.dumps(json_data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(generate_insights(snippet))

    if input("\nWould you like to ask a follow-up question? (y/n): ").strip().lower() == "y":
        question = input("Enter your question: ")
        print("\n--- AI Answer ---")
        print(generate_insights(snippet, question))

if __name__ == "__main__":
    main()
