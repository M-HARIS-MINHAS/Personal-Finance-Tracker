import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSlider>div>div>div>div {
        background-color: #4CAF50;
    }
    .stHeader {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
    }
    .stSubheader {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
    }
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title and Header
st.title("💰 Personal Finance Tracker")
st.subheader("Take Control of Your Finances")

# Introduction
st.write("""
Welcome to your Personal Finance Tracker! This app helps you track your income, expenses, and savings goals. 
Get started by entering your financial details below.
""")

# Section 1: Income and Expenses
st.markdown("### 💵 Income and Expenses")

# Input for income
income = st.number_input("Enter your monthly income (in $):", min_value=0, value=1000)

# Input for expenses
st.write("Enter your monthly expenses (in $):")
expenses = {
    "Rent": st.number_input("Rent", min_value=0, value=1000),
    "Utilities": st.number_input("Utilities", min_value=0, value=200),
    "Groceries": st.number_input("Groceries", min_value=0, value=300),
    "Transportation": st.number_input("Transportation", min_value=0, value=150),
    "Entertainment": st.number_input("Entertainment", min_value=0, value=100),
    "Other": st.number_input("Other", min_value=0, value=50)
}

# Calculate total expenses
total_expenses = sum(expenses.values())
st.write(f"**Total Expenses:** ${total_expenses}")

# Calculate savings
savings = income - total_expenses
st.write(f"**Monthly Savings:** ${savings}")

# Section 2: Visualize Expenses
st.markdown("### 📊 Visualize Your Expenses")

# Bar chart for expenses
expenses_df = pd.DataFrame(list(expenses.items()), columns=["Category", "Amount"])
st.bar_chart(expenses_df.set_index("Category"))

# Pie chart for expenses
fig, ax = plt.subplots()
ax.pie(expenses_df["Amount"], labels=expenses_df["Category"], autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)

# Section 3: Savings Goal Calculator
st.markdown("### 🎯 Savings Goal Calculator")

# Input for savings goal
savings_goal = st.number_input("Enter your savings goal (in $):", min_value=0, value=5000)

# Calculate time to reach goal
if savings > 0:
    months_to_goal = savings_goal / savings
    st.write(f"**Time to reach your goal:** {months_to_goal:.1f} months")
else:
    st.warning("You need to increase your savings to reach your goal.")

# Section 4: Tips for Saving Money
st.markdown("### 💡 Tips for Saving Money")
tips = [
    "Create a budget and stick to it.",
    "Cut down on unnecessary expenses like dining out or subscriptions.",
    "Automate your savings to ensure you save consistently.",
    "Invest in low-cost index funds for long-term growth.",
    "Track your spending regularly to identify areas for improvement."
]
for tip in tips:
    st.write(f"- {tip}")

# Footer
st.markdown("---")
st.write("Built with ❤️ using [Streamlit](https://streamlit.io).")