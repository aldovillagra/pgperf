from typer.testing import CliRunner
from pgperf.pgperf import app
from pgperf.__version__ import __version__


runner = CliRunner()


def test_pgperf_server_configuration_help():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "--help"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_show_all():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "show-all"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_memory():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "memory"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_disk():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "disk"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_kernel():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "kernel"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_vacuum():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "vacuum"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_writer():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "writer"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_file_locations():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "file-locations"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_connection_settings():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "connection-settings"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_authentication():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "authentication"])
    assert result.exit_code == 0


def test_pgperf_server_configuration_ssl():
    result = runner.invoke(
        app, ["--conf", "test", "server", "configuration", "ssl"])
    assert result.exit_code == 0
