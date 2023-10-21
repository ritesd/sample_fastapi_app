import os
from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import text

# Set up a test database
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///./my_test_database.db")
test_database = Database(TEST_DATABASE_URL)