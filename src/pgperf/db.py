from pgperf import env
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
        with engine.begin() as conn:
            conn.execute(SQL)

    def _get_sql(self, name):
        template = env.get_template(name)
        return text(template.render())

    def _get_sql_with_var(self, name, variable):
        template = env.get_template(name)
        return text(template.render(variable=variable))

    def get_from_path(self, path, name):
        return self.read_sql(self._get_sql(path + name + ".sql"))

    def get_from_path_with_var(self, path, name, variable):
        return self.read_sql(
            self._get_sql_with_var(path + name + ".sql", variable))

    def exec_from_path(self, path, name):
        return self.exec(self._get_sql(path + name + ".sql"))
