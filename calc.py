def monthly_compounding(initial, apr, monthly, years):
    final_sum = initial
    apr = apr/100
    monthly_rate = pow(1 + apr, 1/12) - 1
    for _ in range(0, years*12):
        final_sum = final_sum*(1 + monthly_rate) + monthly

    return round(final_sum, 2)