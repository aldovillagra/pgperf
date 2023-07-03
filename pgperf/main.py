from pgperf import console, config, __version__
from pgperf.db import Db
from pgperf.server import app as server_app
from pgperf.index import app as index_app
from pgperf.table import app as table_app
import pandas as pd
import typer

app = typer.Typer()
app.add_typer(server_app, name="server")
app.add_typer(index_app, name="index")
app.add_typer(table_app, name="table")

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
def outliers():
    """
    Queries that have longest execution time in aggregate
    """
    db = Db(state['conf'])
    result = db.outliers()
    console.print(result.to_markdown())


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
