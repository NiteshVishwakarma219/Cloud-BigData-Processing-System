from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("DataTransformationJob") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

print("Original Data:")
df.show()

# Data Transformation: Add GST column (18%)
df_transformed = df.withColumn("GST", col("Amount") * 0.18)

print("Data after GST Transformation:")
df_transformed.show()

# Optional: Save transformed data (for proof)
df_transformed.write.mode("overwrite").csv("output/transformed_data")