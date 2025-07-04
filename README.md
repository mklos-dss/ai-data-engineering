# AI Data Analyst – CLI Application

This command-line tool allows users to upload a JSON file and receive an AI-generated summary and insights, powered by OpenAI's GPT model.

## Features

- Upload structured JSON files
- Receive summaries and insights in natural language
- Ask follow-up questions via the CLI
- Lightweight and fast, no web UI required

## Installation

```bash
git clone https://github.com/mkarasds/data-analyst-ai.git
cd data-analyst-ai
pip install -r requirements.txt
```

## Configuration

Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_key_here
```

Make sure `.env` is listed in `.gitignore`.

## Usage

```bash
python app.py data/sample.json
```

### Example Output

```
--- AI Summary ---
The uploaded JSON includes regional sales figures for Q2. Germany and Poland show strong growth, while the UK is declining slightly.

Would you like to ask a follow-up question? (y/n): y
Your question: What are the biggest risk indicators?

--- AI Answer ---
The decline in the UK region and volatility in France suggest areas for attention in upcoming quarters.
```

## Project Structure

```
.
├── app.py
├── requirements.txt
├── .gitignore
├── .env (not included in repo)
```

---

## Tags

openai, json, cli-tool, ai-analytics, data-analyst, gpt, automation, insights, business-intelligence


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