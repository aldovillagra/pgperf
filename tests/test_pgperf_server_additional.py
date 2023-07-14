from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_server_additional_help():
    result = runner.invoke(
        app, ["--conf", "test", "server", "additional", "--help"])
    assert result.exit_code == 0


def test_pgperf_server_additional_extensions():
    result = runner.invoke(
        app, ["--conf", "test", "server", "additional", "extensions"])
    assert result.exit_code == 0


def test_pgperf_server_additional_add_all_recommended_extensions():
    result = runner.invoke(
        app, ["--conf", "test", "server", "additional", "add-all-recommended-extensions"])
    assert result.exit_code == 0
