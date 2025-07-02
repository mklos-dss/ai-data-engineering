# Data + AI CLI Tool

A simple and secure Python project that connects to the [OpenAI API](https://platform.openai.com/) and analyzes structured data from a JSON file. The application supports `.env` for secure API key storage and allows for both automatic data summarization and interactive questioning.

## Application Features

- Terminal-based interface for communicating with AI (e.g., ChatGPT)
- Secure storage of API key using `.env` file
- Integration with OpenAI Chat Completions API
- Automatic summary of data from a JSON file
- Interactive question mode about the loaded data
- Requirements listed in `requirements.txt` for easy setup
- Lightweight foundation for more advanced data+AI projects

## Technologies

- Python 3.x
- OpenAI API
- Libraries: `openai`, `python-dotenv`

## Installation and Configuration

1. Clone the repository:
   ```
   git clone https://github.com/your-username/data-ai-cli-tool.git
   cd data-ai-cli-tool
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Register at OpenAI:
   - Go to: https://platform.openai.com/docs/overview
   - Create an account
   - In the Billing section, add credit (e.g., $5)
   - Disable "Enable auto recharge" if you don't want automatic top-ups

4. Set up your API key:
   - Go to: https://platform.openai.com/api-keys
   - Generate and copy your API key
   - Copy the `.env_example` file and rename it to `.env`
   - Add your key to the `.env` file:
     ```
     OPENAI_API_KEY=sk-...
     ```
   - Ensure `.env` is added to `.gitignore` to avoid exposing it in your repo

5. Run the application in the terminal:
   ```
   python app.py path/to/yourfile.json
   ```

6. Ask questions:
   - The program will automatically summarize the data
   - Then it will prompt: "Would you like to ask a question about the data? (y/n)"
   - Type your question and receive a contextual AI response

## Project Structure

| File or Folder      | Description                                                |
|---------------------|------------------------------------------------------------|
| `.env`              | File containing your private OpenAI API key               |
| `app.py`            | Main application logic for data+AI analysis via terminal  |
| `requirements.txt`  | List of required Python libraries                         |

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