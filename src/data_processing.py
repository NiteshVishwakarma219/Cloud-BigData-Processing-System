def process_sales(df):

    result = df.groupBy("Region") \
               .sum("Amount")

    print("\n===== REGION SALES SUMMARY =====")
    result.show()

    return result