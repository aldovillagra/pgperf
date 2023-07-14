from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ + '\n' == result.output


def test_config():
    result = runner.invoke(app, ["config"])
    assert result.exit_code == 0
