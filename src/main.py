from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("BigDataProject") \
    .getOrCreate()

# READ DATA
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

df.show()

# FILTER
high_sales = df.filter(col("Amount") > 30000)
high_sales.show()

# TRANSFORM
df2 = df.withColumn("GST", col("Amount") * 0.18)
df2.show()

# AGGREGATE
result = df.groupBy("Region").sum("Amount")
result.show()

# WRITE TO RDS (IMPORTANT)
result.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://YOUR-RDS-ENDPOINT:3306/bigdata_db") \
    .option("dbtable", "sales_summary") \
    .option("user", "admin") \
    .option("password", "YOUR_PASSWORD") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .mode("append") \
    .save()