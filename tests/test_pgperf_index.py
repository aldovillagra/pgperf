from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_index_help():
    result = runner.invoke(app, ["--conf", "test", "index", "--help"])
    assert result.exit_code == 0


def test_pgperf_index_duplicate():
    result = runner.invoke(app, ["--conf", "test", "index", "duplicate"])
    assert result.exit_code == 0


def test_pgperf_index_cache_hit():
    result = runner.invoke(app, ["--conf", "test", "index", "cache-hit"])
    assert result.exit_code == 0


def test_pgperf_index_scans():
    result = runner.invoke(app, ["--conf", "test", "index", "scans"])
    assert result.exit_code == 0


def test_pgperf_index_size():
    result = runner.invoke(app, ["--conf", "test", "index", "size"])
    assert result.exit_code == 0


def test_pgperf_index_usage():
    result = runner.invoke(app, ["--conf", "test", "index", "usage"])
    assert result.exit_code == 0


def test_pgperf_index_null():
    result = runner.invoke(app, ["--conf", "test", "index", "null"])
    assert result.exit_code == 0


def test_pgperf_index_total_size():
    result = runner.invoke(app, ["--conf", "test", "index", "total-size"])
    assert result.exit_code == 0


def test_pgperf_index_unused():
    result = runner.invoke(app, ["--conf", "test", "index", "unused"])
    assert result.exit_code == 0


def test_pgperf_index_all():
    result = runner.invoke(app, ["--conf", "test", "index", "all"])
    assert result.exit_code == 0
