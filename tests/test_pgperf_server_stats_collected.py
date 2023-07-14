from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_server_stats_collected_help():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "--help"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_archiver():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "archiver"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_bgwriter():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "bgwriter"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_database():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "database"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_database_conflicts():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "database-conflicts"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_all_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "all-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_user_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "user-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_xact_all_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "xact-all-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_xact_user_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "xact-user-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_all_indexes():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "all-indexes"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_sys_indexes():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "sys-indexes"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_all_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-all-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_sys_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-sys-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_user_tables():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-user-tables"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_all_indexes():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-all-indexes"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_sys_indexes():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-sys-indexes"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_user_indexes():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-user-indexes"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_all_sequences():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-all-sequences"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_sys_sequences():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-sys-sequences"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_io_user_sequences():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "io-user-sequences"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_user_functions():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "user-functions"])
    assert result.exit_code == 0


def test_pgperf_server_stats_collected_xact_user_functions():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "collected", "xact-user-functions"])
    assert result.exit_code == 0
