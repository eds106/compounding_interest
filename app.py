import streamlit as st
from calc import monthly_compounding

initial = float(input("Input initial amount: "))
apr = float(input("Input APR: "))
monthly = float(input("Input monthly deposits: "))
years = int(input("Input number of years you will invest for: "))

final_sum = monthly_compounding(initial, apr, monthly, years)

print(final_sum)