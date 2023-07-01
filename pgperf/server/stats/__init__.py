from pgperf import config
import typer
from pgperf.server.stats.dinamic import app as dinamic_app
from pgperf.server.stats.collected import app as collected_app

app = typer.Typer()
app.add_typer(dinamic_app, name="dinamic")
app.add_typer(collected_app, name="collected")
state = {"conf": config['prod']}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    The Statistics Collector.
    PostgreSQL's statistics collector is a subsystem that supports collection and reporting of information about server activity. 
    """
    if conf:
        state['conf'] = config[conf]


if __name__ == "__main__":
    app()
