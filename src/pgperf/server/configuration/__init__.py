from pgperf import console, config
from pgperf.db import Db
import typer
from pgperf.server.configuration.replication import app as replication_app

app = typer.Typer()
app.add_typer(replication_app, name="replication")

state = {"conf": config['prod'], "path": "server/config/"}


@app.callback()
def main(verbose: bool = False, debug: bool = False, conf: str = ""):
    """
    Server configuration information
    """
    if conf:
        state['conf'] = config[conf]


def process_with_variables(configs):
    data = {}
    db = Db(state['conf'])
    for conf in configs:
        result = db.get_from_path_with_var(
            state['path'], "show_variable", conf)
        data[conf] = result.iloc[0][conf]
    return data


@app.command()
def show_all():
    """
    Show all Server configuration
    """
    db = Db(state['conf'])
    result = db.get_from_path(state['path'], "show_all")
    console.print(result.to_markdown(), justify="left")


@app.command()
def memory():
    """
    Show Memory configuration
    """
    configs = [
        "shared_buffers", "huge_pages", "huge_page_size", "temp_buffers",
        "max_prepared_transactions", "work_mem", "hash_mem_multiplier",
        "maintenance_work_mem", "autovacuum_work_mem",
        "logical_decoding_work_mem", "max_stack_depth",
        "shared_memory_type", "dynamic_shared_memory_type",
        "min_dynamic_shared_memory"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def disk():
    """
    Show Kernel Resource Usage configuration
    """
    configs = [
        "temp_file_limit"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def kernel():
    """
    Show Kernel configuration
    """
    configs = [
        "max_files_per_process"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def vacuum():
    """
    Show Cost-based Vacuum Delay configuration
    """
    configs = [
        "vacuum_cost_delay", "vacuum_cost_page_hit", "vacuum_cost_page_miss",
        "vacuum_cost_page_dirty", "vacuum_cost_limit"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left",)


@app.command()
def writer():
    """
    Show Background Writer configuration
    """
    configs = [
        "bgwriter_delay", "bgwriter_lru_maxpages", "bgwriter_lru_multiplier",
        "bgwriter_flush_after"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def file_locations():
    """
    Show File Locations configuration
    """
    configs = [
        "data_directory", "config_file", "hba_file", "ident_file", "external_pid_file"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def connection_settings():
    """
    Show Connection Settings configuration
    """
    configs = [
        "listen_addresses", "port", "max_connections", "superuser_reserved_connections",
        "unix_socket_directories", "unix_socket_group", "unix_socket_permissions",
        "bonjour", "bonjour_name", "tcp_keepalives_idle", "tcp_keepalives_interval",
        "tcp_keepalives_count", "tcp_user_timeout", "client_connection_check_interval"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def authentication():
    """
    Show Authentication configuration
    """
    configs = [
        "authentication_timeout", "password_encryption", "krb_server_keyfile", "krb_caseins_users",
        "db_user_namespace"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


@app.command()
def ssl():
    """
    Show Authentication configuration
    """
    configs = [
        "ssl", "ssl_ca_file", "ssl_cert_file", "ssl_crl_file", "ssl_crl_dir", "ssl_key_file", "ssl_ciphers",
        "ssl_prefer_server_ciphers", "ssl_ecdh_curve", "ssl_min_protocol_version", "ssl_min_protocol_version",
        "ssl_dh_params_file", "ssl_passphrase_command", "ssl_passphrase_command_supports_reload"]
    with console.status("Working...", spinner="bouncingBar"):
        data = process_with_variables(configs)
    console.print(data, justify="left")


if __name__ == "__main__":
    app()
