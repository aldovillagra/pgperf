from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_table_help():
    result = runner.invoke(
        app, ["--conf", "test", "table", "--help"])
    assert result.exit_code == 0


def test_pgperf_table_records_rank():
    result = runner.invoke(
        app, ["--conf", "test", "table", "records-rank"])
    assert result.exit_code == 0


def test_pgperf_table_seq_scans():
    result = runner.invoke(
        app, ["--conf", "test", "table", "seq-scans"])
    assert result.exit_code == 0


def test_pgperf_table_cache_hit():
    result = runner.invoke(
        app, ["--conf", "test", "table", "cache-hit"])
    assert result.exit_code == 0


def test_pgperf_table_index_scans():
    result = runner.invoke(
        app, ["--conf", "test", "table", "index-scans"])
    assert result.exit_code == 0


def test_pgperf_table_index_size():
    result = runner.invoke(
        app, ["--conf", "test", "table", "index-size"])
    assert result.exit_code == 0


def test_pgperf_table_size():
    result = runner.invoke(
        app, ["--conf", "test", "table", "size"])
    assert result.exit_code == 0


def test_pgperf_table_size_with_index():
    result = runner.invoke(
        app, ["--conf", "test", "table", "size-with-index"])
    assert result.exit_code == 0


def test_pgperf_table_bloat():
    result = runner.invoke(
        app, ["--conf", "test", "table", "bloat"])
    assert result.exit_code == 0
