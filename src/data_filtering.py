from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("DataFilteringJob") \
    .getOrCreate()

# Load dataset (from local or EC2 path)
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# Show original data
print("Original Data:")
df.show()

# Filtering high value transactions
high_value_df = df.filter(col("Amount") > 30000)

# Show filtered data
print("Filtered High Value Transactions (Amount > 30000):")
high_value_df.show()

# Optional: Save output locally (for proof)
high_value_df.write.mode("overwrite").csv("output/high_value_transactions")