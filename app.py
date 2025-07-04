import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Missing OPENAI_API_KEY in .env file.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

def analyze_data(content, extra_question=None):
    prompt = f"Please analyze the following JSON:\n\n{content}"
    if extra_question:
        prompt += f"\n\nQuestion: {extra_question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an experienced data engineer analyzing JSON data."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <json_file_path>")
        sys.exit(1)

    json_path = sys.argv[1]
    json_data = read_json(json_path)
    preview = json.dumps(json_data, indent=2)[:3500]

    print("\n--- AI Summary ---")
    print(analyze_data(preview))

    if input("\nDo you want to ask a question? (y/n): ").strip().lower() == "y":
        question = input("Enter your question: ")
        print("\n--- AI Answer ---")
        print(analyze_data(preview, question))

if __name__ == "__main__":
    main()
