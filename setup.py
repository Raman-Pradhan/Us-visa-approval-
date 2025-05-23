from setuptools import setup, find_packages

setup(
    name = "us_visa",
    version="0.0.0",
    author="Raman",
    author_email="pradhanraman950@gmail.com",
    packages=find_packages() #it will search for the constructor file("__init__.py") in every folder and wherever it finds it, it will consider it as local package.
) 