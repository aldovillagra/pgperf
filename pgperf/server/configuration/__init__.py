from pgperf import console, config
from pgperf.db import Db
import typer

app = typer.Typer()

state = {"conf": config['prod'], "path": "server/config/"}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    Server configuration information
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def show_all():
    """
    Show all server configuration
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "show_all")
    console.print(result.to_markdown(), justify="left")


if __name__ == "__main__":
    app()
