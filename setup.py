from setuptools import setup

setup(
    name = "puffpan",
    description = "puffpan is a small python module for interacting with a Pufferpanel daemon.",
    version = "1.0",
    author = "powermaker450",
    author_email = "contact@povario.com",
    url = "https://github.com/powermaker450/puff",
    install_requires = ["setuptools", "requests"],
    py_modules = ["pufferpy"],
    license = "MIT"
    )
