# AI Data Integration – JSON CLI Assistant

A command-line utility that integrates artificial intelligence into your data analysis workflow. Upload JSON files and get smart summaries and insights using OpenAI’s GPT models. Ideal for data integration and automation use cases.

## Features

- Upload JSON file via CLI
- Generate descriptive summaries instantly
- Ask follow-up questions about your data
- Lightweight and environment-isolated

## Installation

```bash
git clone https://github.com/dss-mak-her/ai-data-integration.git
cd ai-data-integration
pip install -r requirements.txt
```

## Configuration

Prepare your `.env` file with OpenAI credentials:

```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

```bash
python app.py path/to/your_file.json
```

You’ll receive an AI summary and can ask additional questions interactively.

## Example Output

```
--- AI Summary ---
The JSON contains CRM data from multiple systems. Redundant customer IDs were detected.

Ask a follow-up question? (y/n): y
Your question: Which system has the most duplicates?

--- AI Answer ---
System B has 45 duplicate customer IDs, the highest among all systems.
```

## File Structure

```
├── app.py              # CLI interface
├── .env                # OpenAI credentials (local only)
├── requirements.txt    # Python packages
├── .gitignore          # Ignore .env and cache
```

---

## Tags

openai, json, data-integration, analytics, gpt, cli, ai-assistant, automation


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