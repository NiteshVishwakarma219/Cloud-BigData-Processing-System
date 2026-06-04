from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BigDataProcessing") \
    .getOrCreate()

# STEP 1: LOAD DATA
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# STEP 2: PROCESS DATA
result = df.groupBy("Region").sum("Amount")

# STEP 3: SHOW OUTPUT
result.show()