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
print("Before Data Cleaning") 
# Print Dataframe 
df_pyspark.show() 

# Fill Null values inside Department column with the word 'Generalist' 
df_pyspark = df_pyspark.na.fill('Generalist', subset=['Department']) 

# Assumed Null Value means Employee joined during Company Founding i.e. 2010 
df_pyspark = df_pyspark.na.fill(2010, subset=['Joining Year']) 

# Replace Information Tech with IT 
df_pyspark = df_pyspark.replace( 
	{'Information Tech': 'IT'}, subset=['Department']) 

# Remove Outlier -- We assume 59 to be maximum working age in the company 
df_pyspark = df_pyspark.filter('Age<60') 

# Remove Rows not containing First as well as Last Name 
df_pyspark = df_pyspark.filter( 
	df_pyspark['First Name'].isNotNull() | df_pyspark['Last Name'].isNotNull()) 

print("After Data Cleaning") 
df_pyspark.show() 
