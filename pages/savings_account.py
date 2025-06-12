import streamlit as st
from savingsAccount import SavingsAccount

st.set_page_config(page_title = "SavingsAcct", layout = "centered")
savings = SavingsAccount(200000)

with st.form("savings_form"):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit and operations == "Withdraw":
        with st.spinner("Processing..."):
            savings.withdraw(amount, 5000)

print(savings.balance)