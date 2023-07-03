from pgperf import console, config
from pgperf.db import Db
import typer
from pgperf.server.stats import app as stats_app
from pgperf.server.additional import app as additional_app
from pgperf.server.configuration import app as configuration_all

app = typer.Typer()
app.add_typer(stats_app, name="stats")
app.add_typer(additional_app, name="additional")
app.add_typer(configuration_all, name="configuration")

state = {"conf": config['prod'], "path": "server/"}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    Server Informations 
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def active_conections():
    """
    List all active connections in this moments in your database
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "active_conection")
    console.print(result.to_markdown(), justify="center")


@app.command()
def db_settings():
    """
    Get the DB Settings
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "db_settings")
    console.print(result.to_markdown(), justify="center")


@app.command()
def kill_all(confirm: bool = typer.Option(default=False)):
    """
    Kill all the active database connections
    """
    if confirm:
        db = Db(state['conf'])
        result = db.get_from_path(state['path'], "kill_all")
        console.print(result.to_markdown(), justify="center")


@app.command()
def ssl_used():
    """
    Check if SSL connection is used 
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "ssl_used")
    console.print(result.to_markdown(), justify="center")


@app.command()
def vacuum_stats():
    """
    Dead rows and whether an automatic vacuum is expected to be triggered
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "vacuum_stats")
    console.print(result.to_markdown(), justify="center")


if __name__ == "__main__":
    app()
