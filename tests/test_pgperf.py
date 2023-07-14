from typer.testing import CliRunner
from pgperf.main import app
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
    result = runner.invoke(app, ["--conf", "test", "config"])
    assert result.exit_code == 0


def test_all_locks():
    result = runner.invoke(app, ["--conf", "test", "all_locks"])
    assert result.exit_code == 0


def test_blocking():
    result = runner.invoke(app, ["--conf", "test", "blocking"])
    assert result.exit_code == 0


def test_buffercache_stats():
    result = runner.invoke(app, ["--conf", "test", "buffercache_stats"])
    assert result.exit_code == 0


def test_cache_hits():
    result = runner.invoke(app, ["--conf", "test", "cache_hits"])
    assert result.exit_code == 0


def test_calls():
    result = runner.invoke(app, ["--conf", "test", "calls"])
    assert result.exit_code == 0
