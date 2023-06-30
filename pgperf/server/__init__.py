from pgperf import console, config
from pgperf.db import Db
import typer
from pgperf.server.stats import app as stats_app

app = typer.Typer()
app.add_typer(stats_app, name="stats")
state = {"conf": config['prod']}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    monitor 
    """
    if conf:
        state['conf'] = config[conf]


if __name__ == "__main__":
    app()
