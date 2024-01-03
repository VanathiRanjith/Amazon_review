import sys
from lib import DataManipulation, DataReader, Utils
from pyspark.sql.functions import *
from lib.logger import Log4j

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please specify the environment")
        sys.exit(-1)

    job_run_env = sys.argv[1]

    print("Creating Spark Session ")

    spark = Utils.get_spark_session(job_run_env)

    logger=Log4j(spark)
    #spark.sparkContext.setLogLevel("INFO")
    logger.warn("Created Spark Session")

    ratings_df = DataReader.ratings_df(spark,job_run_env)

    books_df = DataReader.books_df(spark,job_run_env)

    joined_df = DataManipulation.Amazon_df(books_df,ratings_df)

    filtered_results = joined_df.withColumn("categories",regexp_replace(col("categories"),r"[\[\]']", ""))
    aggregated_results = filtered_results.groupBy("categories").agg(count("*").alias("total")).orderBy(col("total").desc())
    aggregated_results.show(50)

    logger.info("this is the end of main")

    #print(aggregated_results.collect())
    #& C:/Users/India/.virtualenvs/Amazonbooksreviewcode-FfKGQYjC/Scripts/python.exe e:/AmazonBooksReview/Amazonbooksreviewcode/application_main.py LOCAL
    #vanathi