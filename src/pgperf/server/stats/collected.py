from pgperf import console, config
from pgperf.db import Db
import typer

app = typer.Typer()
state = {"conf": config['prod'], "path": "server/stats/collected/"}


@app.callback()
def collected(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    Collected Statistics Views 
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def archiver():
    """
    One row only, showing statistics about the WAL archiver process's activity. 
    See pg_stat_archiver for details.
    ( Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_archiver")
    console.print(result.to_markdown(), justify="center")


@app.command()
def bgwriter():
    """
    One row only, showing statistics about the background writer process's activity. 
    See pg_stat_bgwriter for details.
    ( Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_bgwriter")
    console.print(result.to_markdown(), justify="center")


@app.command()
def database():
    """
    One row per database, showing database-wide statistics. 
    See pg_stat_database for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_database")
    console.print(result.to_markdown(), justify="center")


@app.command()
def database_conflicts():
    """
    One row per database, showing database-wide statistics about
    query cancels due to conflict with recovery on standby servers. 
    See pg_stat_database_conflicts for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_database_conflicts")
    console.print(result.to_markdown(), justify="center")


@app.command()
def all_tables():
    """
    One row for each table in the current database, showing statistics
    about accesses to that specific table. 
    See pg_stat_all_tables for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_all_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def user_tables():
    """
    Same as pg_stat_all_tables, except that only user tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_user_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def xact_all_tables():
    """
    Similar to pg_stat_all_tables, but counts actions taken so far within 
    the current transaction (which are not yet included in pg_stat_all_tables
    and related views). The columns for numbers of live and dead rows 
    and vacuum and analyze actions are not present in this view.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_xact_all_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def xact_user_tables():
    """
    Same as pg_stat_xact_all_tables, except that only user tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_xact_user_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def all_indexes():
    """
    One row for each index in the current database, showing statistics
    about accesses to that specific index. See pg_stat_all_indexes
    for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_all_indexes")
    console.print(result.to_markdown(), justify="center")


@app.command()
def sys_indexes():
    """
    Same as pg_stat_all_indexes, except that only indexes on system
    tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_sys_indexes")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_all_tables():
    """
    One row for each table in the current database, showing statistics
    about I/O on that specific table.
    See pg_statio_all_tables for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_all_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_sys_tables():
    """
    Same as pg_statio_all_tables, except that only system tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_sys_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_user_tables():
    """
    Same as pg_statio_all_tables, except that only user tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_user_tables")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_all_indexes():
    """
    One row for each index in the current database, showing statistics 
    about I/O on that specific index. 
    See pg_statio_all_indexes for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_all_indexes")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_sys_indexes():
    """
    Same as pg_statio_all_indexes, except that only indexes on system
    tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_sys_indexes")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_user_indexes():
    """
    Same as pg_statio_all_indexes, except that only indexes on user 
    tables are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_user_indexes")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_all_sequences():
    """
    One row for each sequence in the current database, showing statistics
    about I/O on that specific sequence. See pg_statio_all_sequences 
    for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_all_sequences")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_sys_sequences():
    """
    Same as pg_statio_all_sequences, except that only system sequences 
    are shown. (Presently, no system sequences are defined,
    so this view is always empty.)
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_sys_sequences")
    console.print(result.to_markdown(), justify="center")


@app.command()
def io_user_sequences():
    """
    Same as pg_statio_all_sequences, except that only user sequences 
    are shown.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_statio_user_sequences")
    console.print(result.to_markdown(), justify="center")


@app.command()
def user_functions():
    """
    One row for each tracked function, showing statistics about executions
    of that function. See pg_stat_user_functions for details.
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_user_functions")
    console.print(result.to_markdown(), justify="center")


@app.command()
def xact_user_functions():
    """
    Similar to pg_stat_user_functions, but counts only calls during the
    current transaction (which are not yet included in 
    pg_stat_user_functions).
    (Compatible with PostgresSQL >= 11.0 )
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "pg_stat_xact_user_functions")
    console.print(result.to_markdown(), justify="center")


if __name__ == "__main__":
    app()
