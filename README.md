# AI Data Analyst – Mining Sector CLI Tool

A lightweight command-line application that leverages OpenAI's GPT models to analyze and summarize data from uploaded JSON files. Tailored for mining and heavy industry data operations.

## Features

- Upload a JSON file with operational data
- Get descriptive AI-generated summaries
- Ask custom questions about the data
- All interactions happen locally via CLI

## Installation

```bash
git clone https://github.com/akonieczny-dss/ai-data-analyst-mining.git
cd ai-data-analyst-mining
pip install -r requirements.txt
```

## Configuration

Before use, set your OpenAI API key in a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Make sure `.env` is listed in `.gitignore` to keep your key safe.

## Usage

```bash
python app.py path/to/your_data.json
```

The program will provide an AI summary and optionally allow you to ask follow-up questions.

## Sample Interaction

```
--- AI Summary ---
This JSON contains sensor readings from multiple drill rigs. The system indicates anomalies in temperature data from Drill_Unit_3.

Would you like to ask a follow-up question? (y/n): y
Your question: Are there any performance trends in Drill_Unit_2?

--- AI Answer ---
Yes, performance of Drill_Unit_2 has shown gradual decline over the last 5 days in RPM and fuel efficiency metrics.
```

## File Structure

```
├── app.py
├── .env (excluded)
├── .gitignore
├── requirements.txt
```

---

## Tags

openai, json, data-mining, analytics, gpt, cli, ai-assistant, industrial-ai, mining


**Industry Focus**

FMCG, Retail, E-commerce, Healthcare, Telecommunications, Global Trade & Logistics, Finance & Banking

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