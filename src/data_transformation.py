from pyspark.sql.functions import col

def add_gst(df):

    transformed_df = df.withColumn(
        "GST",
        col("Amount") * 0.18
    )

    print("\n===== GST ADDED =====")
    transformed_df.show()

    return transformed_df