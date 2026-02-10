import subprocess

import jaraco.envs
import pytest


class VirtualEnv(jaraco.envs.VirtualEnv):
    name = ".env"

    def run(self, cmd, *args, **kwargs):
        cmd = [self.exe(cmd[0])] + cmd[1:]
        kwargs = {"cwd": self.root, "encoding": "utf-8", **kwargs}  # Allow overriding
        return subprocess.check_output(cmd, *args, **kwargs)


@pytest.fixture
def venv(tmp_path, monkeypatch):
    """Virtual env with the version of setuptools under test installed"""
    env = VirtualEnv()
    env.root = tmp_path / "venv"
    env.req = "setuptools>=82.0.0"
    # Prevents leaking PYTHONPATH at the environment creation
    monkeypatch.delenv("PYTHONPATH", raising=False)
    return env.create()
