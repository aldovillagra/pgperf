from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_server_stats_dinamic_help():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "--help"])
    assert result.exit_code == 0


def test_pgperf_server_stats_dinamic_activity():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "activity"])
    assert result.exit_code == 0


def test_pgperf_server_stats_dinamic_replication():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "replication"])
    assert result.exit_code == 0


def test_pgperf_server_stats_dinamic_wal_receiver():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "wal-receiver"])
    assert result.exit_code == 0


def test_pgperf_server_stats_dinamic_subscription():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "subscription"])
    assert result.exit_code == 0


def test_pgperf_server_stats_dinamic_ssl():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "ssl"])
    assert result.exit_code == 0


def test_pgperf_server_stats_dinamic_progress_vacuum():
    result = runner.invoke(
        app, ["--conf", "test", "server", "stats", "dinamic", "progress-vacuum"])
    assert result.exit_code == 0
