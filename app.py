import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_engine = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as err:
        print(f"Unable to read file: {err}")
        sys.exit(1)

def get_ai_summary(user_prompt):
    try:
        completion = openai_engine.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You analyze JSON datasets and return human-friendly summaries."},
                {"role": "user", "content": user_prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as err:
        print(f"Error from OpenAI: {err}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    json_path = sys.argv[1]
    parsed_data = load_json_file(json_path)

    snippet = json.dumps(parsed_data, indent=2)[:3000]
    initial_prompt = f"Analyze this JSON data:\n{snippet}\n\nGive a high-level summary."

    print("\n=== Summary ===")
    summary = get_ai_summary(initial_prompt)
    print(summary)

    next_step = input("\nWould you like to ask something specific about this data? (y/n): ").lower().strip()
    if next_step == 'y':
        custom_input = input("Enter your question: ")
        detailed_prompt = f"Here is a JSON document:\n{snippet}\n\nUser question: {custom_input}"
        print("\n=== AI Response ===")
        answer = get_ai_summary(detailed_prompt)
        print(answer)

if __name__ == "__main__":
    main()
