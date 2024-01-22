🌟PYSPARK Practice/Interview Problem 📊
---------------------------------------------
🎯 PROBLEM STATEMENT
---------------------------------------------
Actors and Directors Cooperation
 
Write a PYSPARK program to generate a report that provides pairs (actor_id, director_id) where the actor has cooperated with the director at least 3 times.
 
---------------------------------------------
📝 Schema And Data :
---------------------------------------------
Difficult Level : EASY
 
Input Data :
 
schema = StructType([
StructField("ActorId",IntegerType(),True),
StructField("DirectorId",IntegerType(),True),
StructField("timestamp",IntegerType(),True)
])
 
data = [
(1, 1, 0),
(1, 1, 1),
(1, 1, 2),
(1, 2, 3),
(1, 2, 4),
(2, 1, 5),
(2, 1, 6)
]
 
🚀 Your Task:
Implement a PYSPARK program to find pairs where actors and directors have collaborated at least 3 times.
 
