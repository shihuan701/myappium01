import os
import signal
import subprocess
import time

import pytest


@pytest.fixture(scope='module',autouse=True)
def record_video():
    name = time.time()
    command = f'scrcpy --record {name}.mkv'
    p = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)
