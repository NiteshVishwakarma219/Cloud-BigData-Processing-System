from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("TCS-BigData-Project") \
    .getOrCreate()

# Read from CSV (uploaded file)
df = spark.read.csv("datasets/sales_data.csv", header=True, inferSchema=True)

df.show()

# Filter
high_sales = df.filter(df.Amount > 30000)
high_sales.show()

# Transformation
df2 = df.withColumn("GST", col("Amount") * 0.18)
df2.show()

# Aggregation
result = df.groupBy("Region").sum("Amount")
result.show()

# Write to RDS
result.write \
.format("jdbc") \
.option("url", "jdbc:mysql://RDS-ENDPOINT:3306/bigdata_db") \
.option("dbtable", "sales_summary") \
.option("user", "admin") \
.option("password", "YOUR_PASSWORD") \
.mode("append") \
.save()