# budget_rules.py

RULES = {
    # Global rules
    "Zero-Based": {
        "description": "Allocate every rupee for zero leftover balance",
        "ratios": {},
        "custom_allocation": True,
    },
    "50/30/20": {
        "description": "50% Needs, 30% Wants, 20% Savings",
        "ratios": {
            "Needs": 0.5,
            "Wants": 0.3,
            "Savings": 0.2,
        },
        "custom_allocation": False,
    },

    # India-specific budgeting rules
    "India 70/20/10": {
        "description": "70% Needs + Wants combined, 20% Savings, 10% Insurance/Contingency",
        "ratios": {
            "Needs_Wants": 0.7,
            "Savings": 0.2,
            "Contingency": 0.1,
        },
        "custom_allocation": False,
    },
    "India 40/30/20/10": {
        "description": "40% Expenses, 30% Savings, 20% Goals, 10% Emergency",
        "ratios": {
            "Expenses": 0.4,
            "Savings": 0.3,
            "Goals": 0.2,
            "Emergency": 0.1,
        },
        "custom_allocation": False,
    },
    "India 3-6-9 Emergency": {
        "description": "Emergency fund: 3 months (single), 6 months (family), 9 months (self-employed)",
        "ratios": {},
        "custom_allocation": True,
    },
    "India Reverse Budget": {
        "description": "Save first for goals (housing, education, travel), spend remainder",
        "ratios": {},
        "custom_allocation": True,
    },
    "India 5 Bucket": {
        "description": "50% Needs, 10% Self-growth, 10% Entertainment, 10% Goals, 20% Savings",
        "ratios": {
            "Needs": 0.5,
            "Self_growth": 0.1,
            "Entertainment": 0.1,
            "Goals": 0.1,
            "Savings": 0.2,
        },
        "custom_allocation": False,
    },
    "India Bachat Lakshya": {
        "description": "Save 25-30% income, allocate to goals (emergency fund, travel, housing)",
        "ratios": {},
        "custom_allocation": True,
    },
    "India 12-4-1 Savings": {
        "description": "12x expenses emergency fund, 4x salary in 10 years, 1x salary by 30",
        "ratios": {},
        "custom_allocation": True,
    },
    
    # Add more rules below as needed
}
