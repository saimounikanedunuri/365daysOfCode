# import necessary libraries 
from pyspark.sql import SparkSession 

# Create Spark Session 
sparkSession = SparkSession.builder.appName('g1').getOrCreate() 

# Create Spark DataFrame 
df_pyspark = sparkSession.read.csv( 
	'Employee_Table.csv', 
	header=True, 
	inferSchema=True
) 
# Print Schema 
df_pyspark.printSchema() 

# Print Dataframe 
df_pyspark.show() 

