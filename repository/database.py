import os
from functools import lru_cache
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(env_file, override=True)


sql_client_driver = os.getenv("DB_DRIVER")
connection_string = sql_client_driver \
                    + os.getenv("DATABASE_NAME")

engine = create_engine(connection_string)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


@lru_cache()
def get_db():
    return Session()


