# app.py

import streamlit as st
import pandas as pd
from budget_generator import build_location_aware_prompt, parse_response
from llama_api import call_groq_llama_api

st.set_page_config(page_title="AI Budget Planner", layout="centered")

st.title("💰 AI-Powered Budget Planner")
st.markdown("Plan your monthly budget using AI tailored to your city and income.")

with st.form("budget_form"):
    income = st.number_input("Monthly Income (₹)", min_value=5000, step=1000, value=30000)
    location = st.text_input("Location", value="Uppal, Hyderabad")
    submitted = st.form_submit_button("Generate AI Budget")

if submitted:
    with st.spinner("Generating your personalized budget..."):
        try:
            prompt = build_location_aware_prompt(income, location)
            raw_output = call_groq_llama_api(prompt)
            parsed = parse_response(raw_output)

            st.success("✅ Budget generated successfully!")
            st.subheader(f"📍 {parsed.location} — Rule: {parsed.rule_used}")
            st.markdown(f"**Monthly Income:** ₹{parsed.income:,.0f}")

            for cat in parsed.categories:
                st.markdown(f"### {cat.category} ({cat.percentage}%) — ₹{cat.allocated_amount:,.0f}")
                for item in cat.items:
                    st.markdown(f"- **{item.item}**: {item.amount_range}  \n  _{item.notes}_")
                st.markdown("---")

            st.subheader("💡 Cost Saving Tips")
            for tip in parsed.tips:
                st.markdown(f"- **{tip.title}**: {tip.description}")

            # Export
            df = pd.DataFrame([
                {
                    "Category": cat.category,
                    "Item": item.item,
                    "Amount Range": item.amount_range,
                    "Notes": item.notes
                }
                for cat in parsed.categories
                for item in cat.items
            ])
            st.download_button("📄 Download CSV", df.to_csv(index=False).encode(), "ai_budget.csv", "text/csv")
            st.download_button("📊 Download JSON", raw_output, "ai_budget.json", "application/json")

        except Exception as e:
            st.error(f"❌ Failed to generate budget: {e}")
