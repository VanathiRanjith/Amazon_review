#fixture is to write the setup code and it should be done as part of fixture
import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    spark_session=get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop


#use yield instead of return function to release the resources
    
    