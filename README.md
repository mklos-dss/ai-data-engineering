# JSON Data Analyst CLI

A command-line Python tool for analyzing structured JSON data using the OpenAI API. The app summarizes input data and enables follow-up questions interactively in the terminal.

## Key Features

- Accepts any JSON file as input
- Generates AI-driven summaries
- Asks contextual questions through interactive mode
- Keeps your API key secure via a `.env` file
- Minimal setup, quick insights

## Technology Stack

- Python 3.x
- OpenAI API (GPT-3.5 Turbo)
- Libraries: `openai`, `python-dotenv`

## Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/json-data-analyst-cli.git
cd json-data-analyst-cli
```

2. **Install required packages:**

```bash
pip install -r requirements.txt
```

3. **Create and configure your `.env` file:**

```env
OPENAI_API_KEY=sk-...
```

4. **Run with your JSON file:**

```bash
python app.py data/sample.json
```

## Sample Session

```
--- Summary by AI ---
The data includes 5 user feedback entries. Key themes include praise for UI and dark mode, and issues with performance and login on Android.

Do you want to ask a question about this data? (y/n): y
Type your question: What platforms have the lowest ratings?

--- AI Response ---
Android users reported the lowest ratings, often citing performance problems.
```

## Files Overview

| File             | Purpose                                           |
|------------------|---------------------------------------------------|
| `app.py`         | Main CLI tool that integrates OpenAI API         |
| `.env`           | Your private API key (not uploaded to GitHub)    |
| `example.json`   | Example dataset for testing                      |
| `requirements.txt`| Dependency list                                  |

---

## Tags

**Technologies:** python, cli, openai, dotenv, json, ai  
**Use Cases:** data-summary, insights, analytics, automation  
**Frameworks:** openai, cli-app

---

Built for fast insight generation from your structured data files.


## Enhanced with Data Science Solutions by DS Stream

This project incorporates cutting-edge data science methodologies and advanced analytics techniques developed by [DS Stream](https://www.dsstream.com). Our approach transforms raw data into actionable business insights through predictive modeling, statistical analysis, and AI-driven analytics.

---

## About DS Stream

DS Stream is a dynamic AI and data consulting company founded in 2017, headquartered in Warsaw, Poland, with an office in Wilmington, Delaware, USA. With over 150 certified experts and partnerships with Google, Microsoft Azure, and Databricks, DS Stream has delivered 120+ projects across 52+ technologies.

**Our Expertise**

- 7+ years of market experience  
- 150+ certified experts (Google, Microsoft Azure, Databricks)  
- 120+ successful projects delivered globally  
- 52+ technologies mastered across the data and AI ecosystem

**Core Services**

- **Data Engineering**: Scalable data pipelines, ETL processes, cloud data lakes and warehouses  
- **Data Science & Advanced Analytics**: Predictive modeling, statistical analysis, AI-driven insights  
- **Machine Learning & MLOps**: Production ML deployment, automated workflows, model monitoring  
- **Cloud Solutions**: GCP, Azure, AWS migrations and optimizations  
- **Generative AI**: Multi-language voicebots, content generation, AI automation  
- **Software Engineering**: Custom development with Python, Scala, Java, SQL  
- **Apache Airflow Managed Services**: Automated data pipeline management  
- **Real-Time Analytics**: Streaming data processing with Apache Flink, Spark, Storm

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