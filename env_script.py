#!../env/Scripts/activate.bat python

import subprocess
import sys
from os.path import join, dirname
import os

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'electronic_shop/.env')
load_dotenv(dotenv_path)

PATH = os.getenv('PATH_TO_ENV')

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix


def in_virtualenv():
    """ Check if virtual env is activated """
    return get_base_prefix_compat() != sys.prefix


if in_virtualenv():
    subprocess.call(rf'cmd.exe /k {PATH}deactivate.bat')
else:
    # subprocess.call('python -m venv env')
    subprocess.call(rf'cmd.exe /k {PATH}activate.bat')


