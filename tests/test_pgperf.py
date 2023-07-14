from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--conf", "test", "--help"])
    assert result.exit_code == 0


def test_version():
    result = runner.invoke(app, ["--conf", "test", "version"])
    assert result.exit_code == 0
    assert __version__ + '\n' == result.output


def test_config():
    result = runner.invoke(app, ["--conf", "test", "show-config"])
    assert result.exit_code == 0


def test_all_locks():
    result = runner.invoke(app, ["--conf", "test", "all-locks"])
    assert result.exit_code == 0


def test_blocking():
    result = runner.invoke(app, ["--conf", "test", "blocking"])
    assert result.exit_code == 0


def test_buffercache_stats():
    result = runner.invoke(app, ["--conf", "test", "buffercache-stats"])
    assert result.exit_code == 0


def test_buffercache_usage():
    result = runner.invoke(app, ["--conf", "test", "buffercache-usage"])
    assert result.exit_code == 0


def test_locks():
    result = runner.invoke(app, ["--conf", "test", "locks"])
    assert result.exit_code == 0


def test_long_running_queries():
    result = runner.invoke(app, ["--conf", "test", "long-running-queries"])
    assert result.exit_code == 0
