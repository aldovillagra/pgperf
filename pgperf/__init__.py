__version__ = '0.1.0'

import fire
import os
import sys
from rich.console import Console
from omegaconf import OmegaConf
from jinja2 import Environment, PackageLoader

console = Console()
user_home = os.path.expanduser('~')
config = OmegaConf.load(user_home + '/.pgperf.yml')
file_loader = PackageLoader('pgperf', 'templates')
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

debug = os.getenv('DEBUG')
log = os.getenv('LOG')
conn = os.getenv('CONN')
