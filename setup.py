from setuptools import setup

setup(
    name = "puffpan",
    keywords = ["pufferpanel"],
    description = "puffpan is a small python module for interacting with a Pufferpanel daemon.",
    version = "1.0",
    author = "powermaker450",
    author_email = "contact@povario.com",
    url = "https://github.com/powermaker450/puffpan",
    download_url = "https://github.com/powermaker450/puffpan/archive/refs/tags/v1.0.tar.gz",
    install_requires = ["requests"],
    py_modules = ["puffpan"],
    license = "MIT"
)
