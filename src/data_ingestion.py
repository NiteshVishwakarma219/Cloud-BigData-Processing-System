from pyspark.sql import SparkSession

def load_data():
    spark = SparkSession.builder \
        .appName("BigDataProject") \
        .getOrCreate()

    df = spark.read.csv(
        "datasets/sales_data.csv",
        header=True,
        inferSchema=True
    )

    print("\n===== DATA INGESTION =====")
    df.show()

    return spark, df