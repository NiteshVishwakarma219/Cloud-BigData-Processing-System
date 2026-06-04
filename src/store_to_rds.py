from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("StoreToRDS") \
    .getOrCreate()

# Sample processed data (SAFE WAY)
data = [
    ("North", 75000),
    ("South", 55000),
    ("East", 30000),
    ("West", 55000)
]

columns = ["Region", "Total_Sales"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

df.show()

# RDS Connection
rds_url = "jdbc:mysql://YOUR-RDS-ENDPOINT:3306/bigdata_db"

properties = {
    "user": "admin",
    "password": "YOUR_PASSWORD",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# WRITE TO RDS
df.write.jdbc(
    url=rds_url,
    table="sales_summary",
    mode="append",
    properties=properties
)

print("Data successfully stored in RDS")