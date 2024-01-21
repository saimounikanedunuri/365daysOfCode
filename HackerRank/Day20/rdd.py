from pyspark.sql import SparkSession
spark:SparkSession = SparkSession.builder()
      .master("local[1]")
      .appName("SparkByExamples.com")
      .getOrCreate()   

Create RDD using sparkContext.parallelize()
#Create RDD from parallelize    
data = [1,2,3,4,5,6,7,8,9,10,11,12]
rdd=spark.sparkContext.parallelize(data)

Create RDD using sparkContext.textFile()
#Create RDD from external Data source
rdd2 = spark.sparkContext.textFile("/path/textFile.txt")

Create RDD using sparkContext.wholeTextFiles()
#Reads entire file into a RDD as single record.
rdd3 = spark.sparkContext.wholeTextFiles("/path/textFile.txt")

Create empty RDD using sparkContext.emptyRDD
# Creates empty RDD with no partition    
rdd = spark.sparkContext.emptyRDD 
# rddString = spark.sparkContext.emptyRDD[String]

Creating empty RDD with partition
#Create empty RDD with partition
rdd2 = spark.sparkContext.parallelize([],10) #This creates 10 partitions

RDD Parallelize
print("initial partition count:"+str(rdd.getNumPartitions()))
#Outputs: initial partition count:2

Repartition and Coalesce
reparRdd = rdd.repartition(4)
print("re-partition count:"+str(reparRdd.getNumPartitions()))
#Outputs: "re-partition count:4
