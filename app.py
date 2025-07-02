import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ai_service = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as exc:
        print(f"Error loading JSON: {exc}")
        sys.exit(1)


def call_ai(prompt_text):
    try:
        result = ai_service.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a JSON analyst assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )
        return result.choices[0].message.content
    except Exception as exc:
        print(f"OpenAI API error: {exc}")
        sys.exit(1)


def launch():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    json_data = parse_json(input_path)

    json_snippet = json.dumps(json_data, indent=2)[:3000]  # Limit input size
    base_query = f"Here is a JSON document:\n{json_snippet}\n\nPlease summarize the content."

    print("\n--- AI Summary ---")
    summary_result = call_ai(base_query)
    print(summary_result)

    follow = input("\nWould you like to ask a specific question? (y/n): ").strip().lower()
    if follow == 'y':
        custom_question = input("Enter your question: ").strip()
        detailed_query = f"Here is a JSON document:\n{json_snippet}\n\nQuestion: {custom_question}"
        print("\n--- AI Answer ---")
        answer = call_ai(detailed_query)
        print(answer)


if __name__ == "__main__":
    launch()