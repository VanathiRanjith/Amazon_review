from pyspark.sql.functions import *
from pyspark.sql.functions import regexp_replace, col


def Amazon_df(books_df,ratings_df):
    return books_df.join(ratings_df, "Title")

def Amazon_distinct(Amazon_df):
    a1=Amazon_df.withColumn("authors",regexp_replace(col("authors"),r"[\[\]']", ""))
    a1=Amazon_df.withColumn("categories",regexp_replace(col("categories"),r"[\[\]']", ""))
    return a1

#Most number of books in each genres
def categories_df(Amazon_distinct):
    a1=Amazon_distinct.groupBy("categories").agg(count("*").alias("total")).orderBy(col("total").desc())
    return a1
