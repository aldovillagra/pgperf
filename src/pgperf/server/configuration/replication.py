from pgperf import console, config
from pgperf.db import Db
import typer

app = typer.Typer()
state = {"conf": config['prod'], "path": "server/config/"}


def process_with_variables(configs):
    data = {}
    db = Db(state['conf'])
    for conf in configs:
        result = db.get_from_path_with_var(
            state['path'], "show_variable", conf)
        data[conf] = result.iloc[0][conf]
    return data


@app.callback()
def main(conf: str = ""):
    """
    Server Replication information
    """
    if conf:
        state['conf'] = config[conf]


@app.command()
def sending():
    """
    Show Sending Servers configuration
    """
    configs = [
        "max_wal_senders", "max_replication_slots", "wal_keep_size", "max_slot_wal_keep_size",
        "wal_sender_timeout", "track_commit_timestamp"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def primary():
    """
    Show Primary Server configuration
    """
    configs = [
        "synchronous_standby_names", "vacuum_defer_cleanup_age"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def standby():
    """
    Show Standby Server configuration
    """
    configs = [
        "primary_conninfo", "primary_slot_name", "promote_trigger_file",
        "hot_standby", "max_standby_archive_delay",
        "max_standby_streaming_delay", "wal_receiver_create_temp_slot",
        "wal_receiver_status_interval", "hot_standby_feedback",
        "wal_receiver_timeout", "wal_retrieve_retry_interval",
        "recovery_min_apply_delay"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def subscribers():
    """
    Show Subscribers configuration
    """
    configs = [
        "max_logical_replication_workers", "max_sync_workers_per_subscription"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


if __name__ == "__main__":
    app()
