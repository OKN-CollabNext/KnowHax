from invoke import task


@task
def hello(_):
    print("Hello, world!")


@task
def run(c):
    c.run("taipy run src/knowhax/main.py")
