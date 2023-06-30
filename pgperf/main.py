from pgperf import console, config, __version__
from pgperf.db import Db
from pgperf.server import app as server_app
import pandas as pd
import typer

app = typer.Typer()
app.add_typer(server_app, name="server")

state = {"conf": config['prod']}


@app.callback()
def main(conf: str = ""):
    """
    Python port of [Heroku PG Extras](https://github.com/heroku/heroku-pg-extras) with several additions and improvements.

    The goal of this project is to provide powerful insights into the PostgreSQL database for Python apps that are not using the Heroku PostgreSQL plugin.
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def all_locks():
    """
    List all current locks in your database
    """
    if state['verbose']:
        console.rule("[bold] All the current locks")
    db = Db(state['conf'])
    result = db.all_locks()
    console.print(result.to_markdown(), justify="center")


@app.command()
def bloat():
    """
    Estimation of table 'bloat' space allocated to a relation that is full of dead tuples, that has yet to be reclaimed.
    """
    result = db.bloat()
    console.print(result.to_markdown(), justify="center")


@app.command()
def blocking():
    """
    Get all statements that are currently holding locks in your database
    """
    db = Db(state['conf'])
    result = db.blocking()
    console.print(result.to_markdown(), justify="center")


@app.command()
def buffercache_stats():
    """
    Get all Buffercache Stats
    """
    db = Db(state['conf'])
    result = db.buffercache_stats()
    console.print(result.to_markdown(), justify="center")


@app.command()
def buffercache_usage():
    """
    Get all Buffercache Usage
    """
    db = Db(state['conf'])
    result = db.buffercache_usage()
    console.print(result.to_markdown(), justify="center")


@app.command()
def cache_hits():
    """
    Get all cache hits
    """
    db = Db(state['conf'])
    result = db.cache_hit()
    console.print(result.to_markdown(), justify="center")


@app.command()
def calls_legacy():
    """
    Get the queries that have highest frequency of execution
    """
    # TODO: Pendind test and validate
    db = Db(state['conf'])
    result = db.calls_legacy()
    console.print(result.to_markdown())


@app.command()
def calls():
    """
    Get the queries that have highest frequency of execution
    """
    db = Db(state['conf'])
    result = db.calls()
    console.print(result.to_markdown())


@app.command()
def duplicate_indexes():
    """
    Show multiple indexes that have the same set of columns, same opclass, expression and predicate.
    """
    db = Db(state['conf'])
    result = db.duplicate_indexes()
    console.print(result.to_markdown(), justify="center")


@app.command()
def index_cache_hit():
    """
    Calculates your cache hit rate for reading indexes
    """
    db = Db(state['conf'])
    result = db.index_cache_hit()
    console.print(result.to_markdown(), justify="center")


@app.command()
def index_scans():
    """
    Number of scans performed on indexes
    """
    db = Db(state['conf'])
    result = db.index_scans()
    console.print(result.to_markdown(), justify="center")


@app.command()
def index_size():
    """
    The size of indexes, descending by size, in MB.
    """
    db = Db(state['conf'])
    result = db.index_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def index_usage():
    """
    Index hit rate (effective databases are at 99% and up)
    """
    db = Db(state['conf'])
    result = db.index_usage()
    console.print(result.to_markdown(), justify="center")


@app.command()
def indexes():
    """
    List all the indexes with their corresponding tables and columns.
    """
    db = Db(state['conf'])
    result = db.indexes()
    console.print(result.to_markdown(), justify="center")


@app.command()
def locks():
    """
    Queries with active exclusive locks
    """
    db = Db(state['conf'])
    result = db.locks()
    console.print(result.to_markdown(), justify="center")


@app.command()
def long_running_queries():
    """
    All queries longer than five minutes by descending duration
    """
    db = Db(state['conf'])
    result = db.long_running_queries()
    console.print(result.to_markdown(), justify="center")


@app.command()
def null_indexes():
    """
    Find indexes with a high ratio of NULL values
    """
    db = Db(state['conf'])
    result = db.null_indexes()
    console.print(result.to_markdown(), justify="center")


@app.command()
def outliers():
    """
    Queries that have longest execution time in aggregate
    """
    db = Db(state['conf'])
    result = db.outliers()
    console.print(result.to_markdown())


@app.command()
def records_rank():
    """
    All tables and the number of rows in each ordered by number of rows descending
    """
    db = Db(state['conf'])
    result = db.records_rank()
    console.print(result.to_markdown(), justify="center")


@app.command()
def seq_scans():
    """
    Count of sequential scans by table descending by order
    """
    db = Db(state['conf'])
    result = db.seq_scans()
    console.print(result.to_markdown(), justify="center")


@app.command()
def table_cache_hit():
    """
    Calculates your cache hit rate for reading tables
    """
    db = Db(state['conf'])
    result = db.table_cache_hit()
    console.print(result.to_markdown(), justify="center")


@app.command()
def table_index_scans():
    """
    Count of index scans by table descending by order
    """
    db = Db(state['conf'])
    result = db.table_index_scans()
    console.print(result.to_markdown(), justify="center")


@app.command()
def table_index_size():
    """
    Total size of all the indexes on each table, descending by size
    """
    db = Db(state['conf'])
    result = db.table_index_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def table_size():
    """
    Size of the tables (excluding indexes), descending by size
    """
    db = Db(state['conf'])
    result = db.table_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def total_index_size():
    """
    Total size of all indexes in MB
    """
    db = Db(state['conf'])
    result = db.total_index_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def total_table_size():
    """
    Size of the tables (including indexes), descending by size
    """
    db = Db(state['conf'])
    result = db.total_table_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def unused_indexes():
    """
    Unused and almost unused indexes. Ordered by their size relative to the number of index scans.
    Exclude indexes of very small tables (less than 5 pages), where the planner will almost invariably select a sequential scan,
    but may not in the future as the table grows
    """
    db = Db(state['conf'])
    result = db.unused_indexes()
    console.print(result.to_markdown(), justify="center")


@app.command()
def full_report():
    """
    Generate a full excel report with all info of your database
    """
    reports = [
        "active_conection", "all_locks", "bloat", "blocking",
        "buffercache_stats", "buffercache_usage", "cache_hit",
        "calls", "db_settings", "duplicate_indexes", "extensions",
        "index_cache_hit", "index_scans", "index_size",
        "index_usage", "indexes", "locks", "long_running_queries",
        "null_indexes", "outliers", "records_rank",
        "table_cache_hit", "records_rank", "table_cache_hit",
        "seq_scans", "ssl_used", "table_index_scans",
        "table_index_size", "unused_indexes", "vacuum_stats"]
    writer = pd.ExcelWriter("full_report.xlsx", engine="xlsxwriter")
    db = Db(state['conf'])
    with console.status("[bold green]Working on tasks...") as status:
        while reports:
            report = reports.pop(0)
            expr = "db." + report + "()"
            result = eval(expr)
            date_columns = result.select_dtypes(
                include=['datetime64[ns, UTC]']).columns
            for date_column in date_columns:
                result[date_column] = result[date_column].dt.date
            result.to_excel(writer, sheet_name=report)
            console.print(f"[white]{report} [green] [ Done ]")
    if state['verbose']:
        console.rule("[bold] Writing Report => [bold yellow] full_report.xlsx")
    writer.save()
    if state['verbose']:
        console.rule("[bold green] Done")

# def diagnose():
#     # TODO: table_cache_hit
#     # TODO: index_cache_hit
#     # TODO: unused_indexes
#     # TODO: null_indexes
#     # TODO: bloat
#     # TODO: duplicate_indexes
#     """ PG_EXTRAS_TABLE_CACHE_HIT_MIN_EXPECTED = "0.985"
#         PG_EXTRAS_INDEX_CACHE_HIT_MIN_EXPECTED = "0.985"
#         PG_EXTRAS_UNUSED_INDEXES_MAX_SCANS = 20
#         PG_EXTRAS_UNUSED_INDEXES_MIN_SIZE_BYTES = Filesize.from("1 MB").to_i
#         PG_EXTRAS_NULL_INDEXES_MIN_SIZE_MB = 1 # 1 MB
#         PG_EXTRAS_NULL_MIN_NULL_FRAC_PERCENT = 50 # 50%
#         PG_EXTRAS_BLOAT_MIN_VALUE = 10
#         PG_EXTRAS_OUTLIERS_MIN_EXEC_RATIO = 33 # 33%
#     """
#     pass


@app.command()
def version():
    console.rule("[bold red]PG Extras APP", align="center")
    console.print()
    console.print(
        "[bold] Postgresql Extras APP", justify="center")
    console.print(f"Installed version => {__version__}", justify="center")
    console.print(f"Connected to ==> {config}", justify="center")
    console.print()
    console.rule("[bold red]..::==> Thanks <==::..")


if __name__ == "__main__":
    app()
