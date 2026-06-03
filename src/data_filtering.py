def filter_sales(df):

    high_sales = df.filter(df.Amount > 30000)

    print("\n===== HIGH VALUE SALES =====")
    high_sales.show()

    return high_sales