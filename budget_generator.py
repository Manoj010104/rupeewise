from typing import Dict, List
from pydantic import BaseModel, validator
import re
import json

class BudgetItem(BaseModel):
    item: str
    amount_range: str
    notes: str

class BudgetCategory(BaseModel):
    category: str
    percentage: float
    allocated_amount: float
    items: List[BudgetItem]

class CostSavingTip(BaseModel):
    title: str
    description: str

class LocationBudgetResponse(BaseModel):
    income: float
    location: str
    rule_used: str
    categories: List[BudgetCategory]
    tips: List[CostSavingTip]

    @validator('categories')
    def validate_percentages(cls, v):
        total = sum(cat.percentage for cat in v)
        if not 99.9 <= total <= 100.1:
            raise ValueError(f"Total percentages must sum to 100% (current: {total:.1f}%)")
        return v
def build_location_aware_prompt(income: float, location: str) -> str:
    return f"""Act as a financial advisor specializing in {location}. For a monthly income of ₹{income:,.0f}, create a detailed budget breakdown using the 50/30/20 rule.

Include realistic cost ranges for specific neighborhoods in {location} in these categories:
1. Needs (50%): Housing, groceries, utilities, transportation
2. Wants (30%): Entertainment, dining out, subscriptions
3. Savings/Debt (20%): Emergency fund, investments, debt repayment

Respond with **only** a valid JSON object using this structure:
{{
    "income": {income},
    "location": "{location}",
    "rule_used": "50/30/20",
    "categories": [
        {{
            "category": "Needs",
            "percentage": 50.0,
            "allocated_amount": {income * 0.5},
            "items": [
                {{
                    "item": "Housing",
                    "amount_range": "15,000-25,000",
                    "notes": "1BHK rental prices in {location}"
                }},
                ...other items
            ]
        }},
        ...other categories
    ],
    "tips": [
        {{
            "title": "Shared Housing",
            "description": "Consider sharing a 2BHK in {location} to reduce rent"
        }}
    ]
}}

Requirements:
- All cost ranges must reflect current prices in {location}
- Include specific neighborhoods/suburbs within {location}
- Minimum 3 items per category
- At least 4 location-specific tips
- Escape special characters
- Never reference other cities or locations"""


def parse_response(response: str) -> LocationBudgetResponse:
    try:
        # Remove any surrounding text/markdown
        cleaned = re.sub(r'^[^{]*', '', response, flags=re.DOTALL)
        cleaned = re.sub(r'[^}]*$', '', cleaned, flags=re.DOTALL)
        
        # Parse even if there's trailing commas
        parsed = json.loads(cleaned, strict=False)
        return LocationBudgetResponse(**parsed)
    except Exception as e:
        print(f"Failed response content:\n{response}")
        raise ValueError(f"JSON parsing failed: {str(e)}") from e

# Example usage with debugging
def generate_hyderabad_budget(income: float):
    from your_api_module import call_groq_api  # Replace with actual import
    
    prompt = build_location_aware_prompt(income, "Uppal, Hyderabad")
    response = call_groq_api(
        prompt,
        temperature=0.2,
        max_tokens=1500
    )
    
    print("Raw API Response:\n", response)  # Debugging output
    return parse_response(response)
