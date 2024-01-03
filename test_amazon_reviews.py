import pytest
from lib.DataReader import ratings_df,books_df
from lib.DataManipulation import Amazon_df, Amazon_distinct, categories_df
from pyspark.sql.functions import *
from lib.ConfigReader import get_app_config
import os
from exceptiongroup import BaseExceptionGroup

def test_ratings_df(spark):
    ratings_count=ratings_df(spark,"LOCAL").count()
    assert ratings_count==64579
    
def test_books_df(spark):
    books_count=books_df(spark,"LOCAL").count()
    assert books_count==73820 

#C:/Users/India/.virtualenvs/Amazonbooksreviewcode-FfKGQYjC/Scripts/python.exe -m pytest -m "transformation" -v
#to run transformation only
#whenever you define the marker, you should put it to pytest.ini file
@pytest.mark.transformation()
def test_read_app_config():
    config = get_app_config("LOCAL")
    expected_path = os.path.normpath("data/books_data.csv")
    actual_path = os.path.normpath(config["books.file.path"])
    assert actual_path == expected_path

 #C:/Users/India/.virtualenvs/Amazonbooksreviewcode-FfKGQYjC/Scripts/python.exe -m pytest
#you can use ---@pytest.mark.skip("work in progress")

