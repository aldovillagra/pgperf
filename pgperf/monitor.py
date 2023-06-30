from pgperf import console, config
from pgperf.db import Db
import typer

app = typer.Typer()
state = {"conf": config['prod']}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    monitor 
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def activity():
    """
    One row per server process, showing information related to the current 
    activity of that process, such as state and current query. 
    See pg_stat_activity for details.
    """
    db = Db(state['conf'])
    result = db.pg_stat_activity()
    console.print(result.to_markdown(), justify="center")


@app.command()
def replication():
    """
    One row per WAL sender process, showing statistics about replication 
    to that sender's connected standby server. 
    See pg_stat_replication for details.
    """
    db = Db(state['conf'])
    result = db.pg_stat_replication()
    console.print(result.to_dict(), justify="left")


@app.command()
def wal_receiver():
    """
    Only one row, showing statistics about the WAL receiver from that 
    receiver's connected server. See pg_stat_wal_receiver for details.
    """
    db = Db(state['conf'])
    result = db.pg_stat_wal_receiver()
    console.print(result.to_dict(), justify="left")


@app.command()
def subscription():
    """
    At least one row per subscription, showing information about the 
    subscription workers. 
    See pg_stat_subscription for details.
    """
    db = Db(state['conf'])
    result = db.pg_stat_subscription()
    console.print(result.to_markdown(), justify="left")


@app.command()
def ssl():
    """
    One row per connection (regular and replication), showing information 
    about SSL used on this connection. 
    See pg_stat_ssl for details.
    """
    db = Db(state['conf'])
    result = db.pg_stat_ssl()
    console.print(result.to_markdown(), justify="left")


@app.command()
def progress_vacuum():
    """
    One row for each backend (including autovacuum worker processes) 
    running VACUUM, showing current progress.
    """
    db = Db(state['conf'])
    result = db.pg_stat_progress_vacuum()
    console.print(result.to_markdown(), justify="left")


@app.command()
def statements_reset():
    """
    pg_stat_statements_reset discards statistics gathered so far by 
    pg_stat_statements
    """
    db = Db(state['conf'])
    result = db.pg_stat_statements_reset()
    console.print(result.to_markdown(), justify="center")
