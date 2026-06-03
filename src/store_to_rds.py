def store_data(result):

    result.write \
        .format("jdbc") \
        .option(
            "url",
            "jdbc:mysql://RDS-ENDPOINT:3306/bigdata_db"
        ) \
        .option(
            "dbtable",
            "sales_summary"
        ) \
        .option(
            "user",
            "admin"
        ) \
        .option(
            "password",
            "YOUR_PASSWORD"
        ) \
        .mode("append") \
        .save()

    print("\nData stored successfully in RDS")