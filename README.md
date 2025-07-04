# AI Data Science CLI Tool

A command-line tool designed for data scientists to upload JSON files and get AI-powered summaries and insights using OpenAI's GPT models.

## Features

- Accepts JSON files as input
- Provides AI-generated summaries and interactive Q&A
- Lightweight and fast CLI application
- Secure environment variable handling for API keys

## Installation

```bash
git clone https://github.com/utrackimateusz/ai-data-science.git
cd ai-data-science
pip install -r requirements.txt
```

## Configuration

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Usage

```bash
python app.py path/to/your.json
```

Receive a summary and optionally ask follow-up questions about the data.

## Example Output

```
--- AI Summary ---
The JSON contains experimental results with multiple test runs. Most runs show consistent data, except run 5 which deviates.

Ask a follow-up question? (y/n): y
Your question: What caused the deviation in run 5?

--- AI Answer ---
The deviation appears related to sensor calibration errors during that run.
```

## Project Structure

```
├── app.py
├── requirements.txt
├── .gitignore
├── .env (excluded)
```

---

## Tags

openai, json, data-science, cli, gpt, ai-assistant, automation, research



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