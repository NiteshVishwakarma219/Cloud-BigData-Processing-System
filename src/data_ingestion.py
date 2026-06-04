from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BigData").getOrCreate()

df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

df.show()