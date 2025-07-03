import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY not found in environment variables.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to read JSON file: {e}")
        sys.exit(1)

def get_analysis(prompt, question=None):
    full_prompt = f"Analyze this JSON data:\n\n{prompt}"
    if question:
        full_prompt += f"\n\nFollow-up question: {question}"

    try:
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert data analyst. Provide useful summaries and insights."},
                {"role": "user", "content": full_prompt}
            ]
        )
        return chat.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    json_data = load_json(filepath)
    snippet = json.dumps(json_data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(get_analysis(snippet))

    if input("\nDo you want to ask a follow-up question? (y/n): ").lower() == "y":
        followup = input("Your question: ")
        print("\n--- AI Answer ---")
        print(get_analysis(snippet, followup))

if __name__ == "__main__":
    main()
