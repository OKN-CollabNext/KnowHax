from invoke import task


@task
def hello(_):
    print("Hello, world!")


@task
def build(c):
    c.run("cd observable && yarn build")


@task
def run(c):
    c.run("cd observable && yarn dev")


@task
def deploy(c):
    c.run("cd observable && yarn deploy")
