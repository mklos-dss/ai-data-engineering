# AI Data Analyst Engineer – CLI Tool

This CLI-based tool allows you to upload a JSON file and receive structured summaries or answers from OpenAI’s GPT model. It is designed for engineers and analysts who want fast insights from data files without writing custom code.

## Features

- Accepts any JSON file as input
- Provides AI-generated summary and insights
- Allows follow-up questions interactively
- Lightweight CLI utility with zero UI dependencies
- Environment-safe OpenAI API key loading

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/piotr-lotka-dss/ai-data-analyst-engineer.git
   cd ai-data-analyst-engineer
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ```

## Usage

Run the tool by passing a `.json` file:

```
python app.py data/example.json
```

You’ll first get an automatic summary, followed by an optional question prompt.

## Sample Output

```
--- Summary ---
This JSON file contains 200 log entries from a web application.
Most entries show 200 status codes, with occasional 404s on static files.

Ask a question about this data? (y/n): y
Enter your question: Which endpoints failed the most?

--- Answer ---
The /images/logo.png and /scripts/app.js endpoints returned the most 404 errors.
```

## File Structure

```
├── app.py              # Python script for AI interaction
├── .env                # Your private API key
├── .gitignore          # Ignores .env and cache files
├── requirements.txt    # Python dependencies
├── example.json        # Sample test file (optional)
```

---

## Tags

cli, openai, json, data-analysis, engineers, terminal-tool, gpt, automation


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