from invoke import task


@task
def hello(c):
    print("Hello, world!")
