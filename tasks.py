from invoke import task


@task
def hello(_):
    print("Hello, world!")

@task
def install(c):
    c.run("cd observable && yarn install")

@task
def build(c):
    c.run("cd observable && yarn build")


@task
def run(c):
    c.run("cd observable && yarn dev")


@task
def deploy(c):
    c.run("cd observable && yarn deploy")


@task
def clean_branches(c):
    c.run("git branch | grep -v 'main' | xargs git branch -D")
