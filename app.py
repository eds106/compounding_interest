import streamlit as st
from calc import monthly_compounding

initial = float(input("How much money are you starting with: "))
apr = float(input("What interest will you compound annually: "))
monthly = float(input("How much will you deposit monthly: "))
years = int(input("How many years will you be invested for: "))

final_sum = monthly_compounding(initial, apr, monthly, years)

print(final_sum)