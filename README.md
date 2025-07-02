# JSON Insight Assistant

A lightweight Python CLI application that reads a local JSON file, connects to the OpenAI API, and generates intelligent insights. It offers automatic summarization and an interactive mode to ask follow-up questions about the dataset.

## Features

- Reads a `.json` file provided by the user
- Generates a smart summary using GPT-3.5-Turbo
- Interactive terminal question mode
- Secure OpenAI API key via `.env`
- Lightweight, easy to use and extend

## Technologies

- Python 3.x
- OpenAI API
- `python-dotenv`, `openai`

## Installation

1. **Clone this repository:**

```bash
git clone https://github.com/Evgeniy-Yakubovskiy/ds-stream.git
cd json-insight-assistant
```

2. **Install required packages:**

```bash
pip install -r requirements.txt
```

3. **Configure your OpenAI API key:**

- Copy the `.env_example` file to `.env`
- Inside `.env`, add your API key:

```env
OPENAI_API_KEY=sk-...
```

4. **Run the tool with your JSON file:**

```bash
python app.py data/example.json
```

## Example Usage

```
--- Summary by AI ---
The dataset includes 5 feedback entries from users across iOS, Android, and Web. Common issues include slow loading and crashes, while dark mode received praise.

Do you want to ask a question about this data? (y/n): y
Type your question: What is the most common complaint?

--- AI Response ---
The most frequent complaint concerns slow app loading and crashes, especially on Android.
```

## File Overview

| File              | Description                                    |
|-------------------|------------------------------------------------|
| `app.py`          | Main Python CLI script                         |
| `.env`            | Environment file for API key (excluded from Git) |
| `example.json`    | Sample dataset to test                         |
| `requirements.txt`| List of Python dependencies                   |

---

## Tags

**Technologies:** python, cli, openai, dotenv, data-processing, language-models  
**Industries:** public-sector, analytics, fintech, automation  
**Frameworks:** openai, cli-app, json

---

Crafted as a simple starting point for intelligent data analysis workflows using AI.

## About the Project

This project can be used as a base for more advanced applications that combine structured data with large language models:

- Automatic document or report generation
- Interactive chatbots with data context
- Smart assistants for form processing
- AI-powered text analysis or classification
- Intelligent decision support tools

---

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

**Headquarters:**  
Warsaw, Poland | Wilmington, Delaware, USA

---

## Technologies Used

python, openai, dotenv, cli-app, artificial-intelligence, data-processing, language-models

## Industry Tags

public-sector, grants, automation, fintech, civic-tech

## Framework Tags

python, dotenv, cli, openai