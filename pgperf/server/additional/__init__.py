from pgperf import console, config
from pgperf.db import Db
import typer

app = typer.Typer()

state = {"conf": config['prod'], "path": "server/additional/"}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    Additional Supplied Modules 
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def extensions():
    """
    Get available and installed extensions
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "extensions")
    console.print(result.to_markdown(), justify="center")


@app.command()
def add_all_recommended_extensions():
    """
    Adding Extensions [sslinfo, pg_buffercache, pg_stat_statements] to your database.
    """
    db = Db(state['conf'])
    db.exec_from_path(state['path'], "add_al")
    db.add_extensions()


if __name__ == "__main__":
    app()
