from pgperf import console, config
from pgperf.db import Db
import typer

app = typer.Typer()

state = {"conf": config['prod'], "path": "server/"}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    Table Informations 
    """
    if conf:
        state['conf'] = config[conf]


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
def cache_hit():
    """
    Calculates your cache hit rate for reading tables
    """
    db = Db(state['conf'])
    result = db.table_cache_hit()
    console.print(result.to_markdown(), justify="center")


@app.command()
def index_scans():
    """
    Count of index scans by table descending by order
    """
    db = Db(state['conf'])
    result = db.table_index_scans()
    console.print(result.to_markdown(), justify="center")


@app.command()
def index_size():
    """
    Total size of all the indexes on each table, descending by size
    """
    db = Db(state['conf'])
    result = db.table_index_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def size():
    """
    Size of the tables (excluding indexes), descending by size
    """
    db = Db(state['conf'])
    result = db.table_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def size_with_index():
    """
    Size of the tables (including indexes), descending by size
    """
    db = Db(state['conf'])
    result = db.total_table_size()
    console.print(result.to_markdown(), justify="center")


@app.command()
def bloat():
    """
    Estimation of table 'bloat' space allocated to a relation that is full of dead tuples, that has yet to be reclaimed.
    """
    result = db.bloat()
    console.print(result.to_markdown(), justify="center")


if __name__ == "__main__":
    app()
