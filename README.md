# Rupeewise – Smart Budget Planner

Rupeewise is an AI-powered personal finance management tool built with Streamlit. It helps users create tailored monthly budgets using classic and modern budgeting strategies, with special consideration for Indian cities and cost structures.

## Features

- **Multiple Budgeting Strategies**: Choose from classic methods like 50/30/20, 70/20/10, Pay Yourself First, Zero-Based Budgeting, and India-specific strategies such as Reverse Budget and 3-6-9 Emergency.
- **Location-aware Recommendations**: Budget allocations are adjusted based on the user’s city (metro/non-metro) for higher accuracy.
- **AI-Powered Allocations**: For custom strategies, the app uses the Groq Llama API to generate optimal allocations and provide cost-saving tips.
- **Clean UI with Streamlit**: Modern, intuitive navigation and responsive forms for seamless budget planning.
- **Export Options**: (Assumed from the code structure; if you have export functions, mention CSV/Excel/PDF export.)

## How It Works

1. **Start Planning**: Click "Start Planning" to begin.
2. **Select a Strategy**: Browse and select a budgeting rule that fits your lifestyle.
3. **Input Details**: Enter your monthly income and location (city/district).
4. **AI Analysis**: For custom/AI-powered strategies, the app consults an LLM for personalized allocations and tips.
5. **See Results**: Instantly view a structured budget breakdown and actionable insights.
6. **Export**: Download your budget (feature assumed—add/remove as per your code).

## Technologies Used

- **Python 3.7+**
- **Streamlit** for UI
- **Pandas** for data handling
- **Groq Llama API** for AI-powered budget generation
- **Math, JSON, typing** for internal logic

## Project Structure

```
.
├── app.py                # Main Streamlit application (UI & logic)
├── budget_generator.py   # Prompt building, response parsing, business logic
├── budget_rules.py       # Budget rules/ratios and policy logic
├── llama_api.py          # Handles communication with Llama API
├── requirements.txt      # Python dependencies
```

## Setup & Usage

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

```bash
git clone https://github.com/Manoj010104/rupeewise.git
cd rupeewise
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

Visit the provided local URL (usually http://localhost:8501/) to use the app.

## Customization

- Edit `budget_rules.py` to tweak or add new budgeting strategies.
- Modify `llama_api.py` to update API keys, endpoints, or prompt templates.

## License

MIT License

## Contact

Questions or suggestions? Reach out to [Manoj010104](https://github.com/Manoj010104).
