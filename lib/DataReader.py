from lib import ConfigReader

#defining ratings schema
def get_ratings_schema():
    schema = 'Id int,Title string,Price string,User_id string,profileName string,review_helpfulness string,review_score string,review_time string,review_summary string,review_text string'
    return schema

# creating ratings dataframe
def ratings_df(spark,env):
    conf = ConfigReader.get_app_config(env)
    ratings_file_path = conf["ratings.file.path"]
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_ratings_schema()) \
        .load(ratings_file_path)

#defining books schema
def get_books_schema():
    schema = 'Title string, description string, authors string, image string, previewLink string, publisher string, publishedDate string, infoLink string, categories string, ratingsCount string'
    return schema

# creating books dataframe
def books_df(spark,env):
    conf = ConfigReader.get_app_config(env)
    books_file_path = conf["books.file.path"]
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_books_schema()) \
        .load(books_file_path)
