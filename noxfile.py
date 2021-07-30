import nox


@nox.session()
def test(session):
    session.install("pytest", "mock", "pytest-mock", "flask", "pytest-cov", "coverage")
    session.install("-r", "requirements.txt")
    session.install("-e", "./model/")
    if session.posargs:
        session.run("pytest", *session.posargs, external=True)
    else:
        session.run("pytest", "tests/", "--cov=model", "--junitxml=report.xml", external=True)
