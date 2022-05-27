import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Db():
    def __init__(self, config):
        self.config = config["db"]
        conf = self.config
        string_connection = "postgresql://" + conf["user"] + ":"
        string_connection += conf["password"] + "@" + conf["server"] + ":"
        string_connection += str(conf["port"]) + "/" + conf["db"]
        self.string_connection = string_connection

    def read_sql(self, SQL, parametros=None):
        engine = create_engine(self.string_connection)
        return pd.read_sql(SQL, params=parametros, con=engine)

    def exec(self, SQL):
        engine = create_engine(self.string_connection)
        engine.execute(SQL)
