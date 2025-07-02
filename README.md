# AI Data Analyst CLI

A streamlined Python CLI utility for analyzing structured JSON files using the OpenAI API. Instantly summarize your data and ask contextual questions through an interactive terminal interface.

## Features

- Accepts local `.json` file uploads
- Automatically summarizes content via GPT-3.5
- Interactive mode for follow-up questions
- Secure API key via `.env` file
- Easy to set up and modify

## Technology Stack

- Python 3.11+
- OpenAI GPT API
- `openai`, `python-dotenv`

## Getting Started

1. **Clone this repository:**

```bash
git clone https://github.com/michalmilosz-ds/ai-data-analyst.git
cd ai-data-analyst
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Prepare your OpenAI API key:**

```env
OPENAI_API_KEY=sk-...
```

4. **Run the app:**

```bash
python app.py path/to/yourfile.json
```

## Example Output

```
=== Summary ===
This dataset includes user feedback entries from mobile and web platforms. Common issues are related to app crashes and load speed, while dark mode and usability are praised.

Would you like to ask something specific about this data? (y/n): y
Enter your question: Which platform had the most complaints?

=== AI Response ===
Android received the most complaints, mostly regarding performance and crashes.
```

## Project Structure

| File             | Description                                |
|------------------|--------------------------------------------|
| `app.py`         | CLI logic for JSON analysis with OpenAI     |
| `.env`           | API key file (not committed)               |
| `example.json`   | Sample dataset                             |
| `requirements.txt`| Project dependencies                      |

---

## Tags

**Technologies:** python, openai, cli, dotenv, json, ai  
**Use Cases:** data-insights, auto-summary, structured-data, terminal-app  
**Frameworks:** openai, cli

---

Created for rapid insight generation from real-world structured datasets.


**Industry Focus**

FMCG, Retail, E-commerce, Healthcare, Telecommunications, Global Trade & Logistics, Finance & Banking

---

## Contact DS Stream

Ready to turn your data into business value? Reach out to DS Stream experts:

- Website: [www.dsstream.com](https://www.dsstream.com)
- LinkedIn: [DS Stream Company Page](https://www.linkedin.com/company/dsstream/)
- [Explore Our Services](https://www.dsstream.com/services)
- [View Our Projects](https://www.dsstream.com/projects)
- [Data Engineering](https://www.dsstream.com/services/data-engineering)


**Headquarters:**  
Warsaw, Poland | Wilmington, Delaware, USA

---

## Technologies Used

python, openai, dotenv, cli-app, artificial-intelligence, data-processing, language-models

## Industry Tags

public-sector, grants, automation, fintech, civic-tech

## Framework Tags

python, dotenv, cli, openai