from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_server_help():
    result = runner.invoke(
        app, ["--conf", "test", "server", "--help"])
    assert result.exit_code == 0


def test_pgperf_server_active_conections():
    result = runner.invoke(
        app, ["--conf", "test", "server", "active-conections"])
    assert result.exit_code == 0


def test_pgperf_server_db_settings():
    result = runner.invoke(
        app, ["--conf", "test", "server", "db-settings"])
    assert result.exit_code == 0


def test_pgperf_server_db_kill_all():
    result = runner.invoke(
        app, ["--conf", "test", "server", "kill-all"])
    assert result.exit_code == 0


def test_pgperf_server_db_ssl_used():
    result = runner.invoke(
        app, ["--conf", "test", "server", "ssl-used"])
    assert result.exit_code == 0


def test_pgperf_server_db_vacuum_stats():
    result = runner.invoke(
        app, ["--conf", "test", "server", "vacuum-stats"])
    assert result.exit_code == 0
