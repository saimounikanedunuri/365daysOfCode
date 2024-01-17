# Dropping Entire rows containing Null 
null_dropped=df_pyspark.na.drop() 
null_dropped.show()

subset in dataframe:
# Dropping Rows where Joining Year is missing 
non_null_year = df_pyspark.na.drop(subset=['Joining Year']) 
non_null_year.show()

fill null values:
# Fill Null values inside Department column with the word 'Generalist' 
df_pyspark.na.fill('Generalist',subset=['Department']).show()
