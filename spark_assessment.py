# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#enter the file path here
file_path = "/datasets/orders.json"

#read the file
df = spark.read.json(file_path, multiLine=True)

# Explode Products
df = df.withColumn(
  'products',
  f.explode(df.products)  
)

# 
df = df.\
  withColumn(
    'product_name',
    f.col('products.product_name')).\
  withColumn(
    'product_price',
    f.col('products.product_price')).\
  drop(df.products)

# Display the final DataFrame using the display() function.
display(df)
