import contextlib
import os
from pathlib import Path

from invoke import task


# context manager that make sure subsequent
# commands are run in the specified directory
@contextlib.contextmanager
def cwd(rel_path: str):
    prev_cwd = os.getcwd()
    try:
        os.chdir(Path(__file__).parent / rel_path)
        yield
    finally:
        os.chdir(prev_cwd)


@task
def hello(_):
    print("Hello, world!")


@task
def install(c):
    with cwd("observable"):
        c.run("yarn install")


@task
def build(c):
    with cwd("observable"):
        c.run("yarn build")


@task
def dev(c):
    with cwd("observable"):
        c.run("yarn dev")


@task
def deploy(c):
    with cwd("observable"):
        c.run("yarn deploy")


@task
def clean_branches(c):
    c.run("git branch | grep -v 'main' | xargs git branch -D")


@task
def touch(c):
    with cwd("observable/docs/data"):
        c.run("touch graph.sqlite.py")


@task
def fetch(c):
    with cwd("."):
        c.run("python scripts/fetch_custom_institutions.py hbcus 5")
