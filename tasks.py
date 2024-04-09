from invoke import task


@task
def hello(_):
    print("Hello, world!")
