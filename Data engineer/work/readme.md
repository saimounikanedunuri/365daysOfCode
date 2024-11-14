# AWS Data Engineering: Daily Techniques and Best Practices

In data engineering, maintaining organized, traceable processes is essential. Below are some practical techniques with examples that can streamline workflows and enhance clarity.

## 1. **Generating Unique IDs for Script Runs**
A unique ID for each script run helps in distinguishing individual executions, especially useful for logging and troubleshooting.

```python
import uuid
script_run_id = str(uuid.uuid4()) ``` # Creates a unique identifier for each script run

## 2. **Counting Active Files**
Tracking how many files are actively being processed at any time provides a quick snapshot of workflow progress, particularly helpful with large datasets.

```python
global Active_Files_Count ```  # Track the number of files processed

## 3. **Metadata Tables**
Metadata tables store important information about datasets, including their origin, state, and transformation details. This helps ensure data quality and makes it easier to trace specific information about data sources and transformations.

## 4. **Organized Logging Setup**
A structured logging setup captures all critical details from each script run, enabling real-time monitoring and providing a history for debugging and performance analysis.

```python
import logging
import time

log_file = "process.log"
logging.basicConfig(
    filename=log_file,
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(name)-25s - %(threadName)-12s - %(levelname)-5s - %(message)s'
)
logging.getLogger().addHandler(logging.StreamHandler())

The log captures:

Timestamp: When each action occurs.
Thread Name: Useful for scripts running multiple tasks.
Message: Provides context for each action.

## 5. **Recording Script Start Times**
Logging the script’s start time aids in performance analysis by highlighting the time taken for each phase of the data process.

```python
start_time = str(time.strftime("%H:%M:%S"))  # Record the script's start time

These techniques make data workflows more organized, traceable, and easier to manage. 
