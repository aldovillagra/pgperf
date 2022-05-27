from pgperf import console, fire, config, debug, log, conn, __version__, env
from pgperf.db import Db
from sqlalchemy.sql import text


class CliTools(object):
    def __init__(self) -> None:
        if not conn:
            self.config = config['prod']
        else:
            self.config = config[conn]
        self.db = Db(self.config)

    def _get_sql(self, name):
        template = env.get_template(name)
        return text(template.render())

    def add_extensions(self):
        console.rule("[bold] pg_stat_statements extension enabled?")
        self.db.exec(self._get_sql("add_extensions.sql"))
        console.rule()

    def all_locks(self):
        console.rule("[bold] All the current locks")
        result = self.db.read_sql(self._get_sql("all_locks.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def bloat(self):
        console.rule(
            "[bold] Estimation of table 'bloat' space allocated to a relation that is full of dead tuples, that has yet to be reclaimed.")
        result = self.db.read_sql(self._get_sql("bloat.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def blocking(self):
        console.rule("[bold] Statements that are currently holding locks.")
        result = self.db.read_sql(self._get_sql("blocking.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def buffercache_stats(self):
        console.rule("[bold] Buffercache Stats.")
        result = self.db.read_sql(
            self._get_sql("buffercache_stats.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def buffercache_usage(self):
        console.rule("[bold] Buffercache Stats.")
        result = self.db.read_sql(self._get_sql("buffercache_usage.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def cache_hits(self):
        console.rule("[bold] Index hit rate / Table hit rate")
        result = self.db.read_sql(self._get_sql("cache_hit.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def calls_legacy(self):
        console.rule(
            "[bold] Statements, like outliers but ordered by the number of times a statement")
        result = self.db.read_sql(self._get_sql("calls_legacy.sql"))
        console.print(result.to_markdown())
        console.rule()

    def calls(self):
        console.rule(
            "[bold] Statements, like outliers but ordered by the number of times a statement")
        result = self.db.read_sql(self._get_sql("calls.sql"))
        console.print(result.to_markdown())
        console.rule()

    def db_settings(self):
        console.rule("[bold] DB Settings")
        result = self.db.read_sql(self._get_sql("db_settings.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def duplicate_indexes(self):
        console.rule("[bold] pg_stat_statements extension enabled?")
        result = self.db.read_sql(self._get_sql("duplicate_indexes.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def extensions(self):
        console.rule("[bold] pg_stat_statements extension enabled?")
        result = self.db.read_sql(self._get_sql("extensions.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_cache_hit(self):
        console.rule("[bold] Table's indexes cache")
        result = self.db.read_sql(self._get_sql("index_cache_hit.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_scans(self):
        console.rule("[bold] Table's indexes scans")
        result = self.db.read_sql(self._get_sql("index_scans.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_size(self):
        console.rule(
            "[bold] Size of each each index in the database, in MB, in MB.")
        result = self.db.read_sql(self._get_sql("index_size.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_usage(self):
        console.rule("[bold] Efficiency of index_usage")
        result = self.db.read_sql(self._get_sql("index_usage.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def indexes(self):
        console.rule("[bold] Efficiency of indexes")
        result = self.db.read_sql(self._get_sql("indexes.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def kill_all(self):
        console.rule("[bold] KILL ALL SESSIONs")
        self.db.exec(self._get_sql("kill_all.sql"))
        console.rule()

    def locks(self):
        console.rule("[bold] Exclusive lock on a relation")
        result = self.db.read_sql(self._get_sql("locks.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def long_running_queries(self):
        console.rule(
            "[bold] Currently running queries, that have been running for longer than 5 minutes, descending by duration.")
        result = self.db.read_sql(self._get_sql("long_running_queries.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def null_indexes(self):
        console.rule("[bold] Displays indexes that contain NULL values.")
        result = self.db.read_sql(self._get_sql("null_indexes.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def outliers(self):
        console.rule("[bold] Statements, obtained from pg_stat_statements")
        result = self.db.read_sql(self._get_sql("outliers.sql"))
        console.print(result.to_markdown())
        console.rule()

    def pg_stat_statements_reset(self):
        console.rule("[bold] PostgreSQL Stat Statements Reset")
        self.db.exec(self._get_sql("pg_stat_statements_reset.sql"))
        console.rule()

    def records_rank(self):
        console.rule(
            "[bold] Estimated count of rows per table, descending by estimated count..")
        result = self.db.read_sql(self._get_sql("records_rank.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_cache_hit(self):
        console.rule("[bold] Table's cache hit")
        result = self.db.read_sql(self._get_sql("table_cache_hit.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def seq_scans(self):
        console.rule(
            "[bold] Number of sequential scans recorded against all tables, descending by count of sequential scans.")
        result = self.db.read_sql(self._get_sql("seq_scans.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def ssl_used(self):
        console.rule(
            "[bold] Number of SSL client.")
        result = self.db.read_sql(self._get_sql("ssl_used.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_index_scans(self):
        console.rule("[bold] Total Index Scans.")
        result = self.db.read_sql(self._get_sql("table_index_scans.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_index_size(self):
        console.rule(
            "[bold] Total size of all indexes on the database, in MB.")
        result = self.db.read_sql(self._get_sql("table_index_size.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_size(self):
        console.rule(
            "[bold] Size of each table and materialized view in the database, in MB.")
        result = self.db.read_sql(self._get_sql("table_size.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def total_index_size(self):
        console.rule(
            "[bold] Total size of indexes for each table and materialized view, in MB.")
        result = self.db.read_sql(self._get_sql("total_index_size.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def total_table_size(self):
        console.rule(
            "[bold] Size of each table and materialized view in the database, in MB.")
        result = self.db.read_sql(self._get_sql("total_table_size.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def unused_indexes(self):
        console.rule(
            "[bold] Indexes that have < 50 scans recorded against them, and are greater than 5 pages in size.")
        result = self.db.read_sql(self._get_sql("unused_indexes.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def vacuum_stats(self):
        console.rule(
            "[bold] Statistics related to vacuum operations for each table, including an estimation of dead rows.")
        result = self.db.read_sql(self._get_sql("vacuum_stats.sql"))
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def version(self):
        console.rule("[bold red]PG Perf APP", align="left")
        console.print()
        console.print(
            "[bold] Postgresql Performance Analysis APP", justify="center")
        console.print(f"Installed version => {__version__}", justify="center")
        console.print(f"Connected to ==> {self.config}", justify="center")
        console.print()
        console.rule("[bold red]..::==> Thanks <==::..")


def run():
    fire.Fire(CliTools)
