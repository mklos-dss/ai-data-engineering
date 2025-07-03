# HK AI Data Analyst CLI

A lightweight command-line app for summarizing and querying structured JSON data using the OpenAI GPT API.

## Features

- Accepts a local JSON file and outputs a human-readable summary
- Asks AI follow-up questions through an interactive interface
- Requires only Python and an OpenAI API key stored in `.env`

## Technologies

- Python 3.10+
- OpenAI GPT-3.5 Turbo
- Libraries: `openai`, `python-dotenv`

## Setup

```bash
git clone https://github.com/hubert-kujawa/hk-ai-data-analyst.git
cd hk-ai-data-analyst
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-...
```

## Usage

```bash
python app.py example.json
```

You’ll get a structured summary and an optional Q&A prompt.

### Sample Output

```
=== AI Summary ===
This file includes customer reviews across multiple platforms, highlighting usability issues and common requests for performance improvements.

Do you want to ask a question about this data? (y/n): y
Enter your question: Which feedback type is most positive?

=== AI Answer ===
Positive comments mainly relate to the interface design and ease of navigation.
```

## File Structure

| File              | Description                              |
|-------------------|------------------------------------------|
| `app.py`          | The CLI tool logic                        |
| `.env`            | API key config (not pushed to GitHub)     |
| `requirements.txt`| Project dependencies                      |

---

## Tags

**Technologies:** python, openai, cli, json, dotenv  
**Use Cases:** interactive-data-analysis, JSON summarization  
**Frameworks:** openai, terminal

---

Developed for HK by leveraging the power of OpenAI for smarter JSON analysis.


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