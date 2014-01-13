from setuptools import setup, find_packages

setup(
    name="escape",
    version="0.1.0",
    description="A classic text-based escape adventure",
    long_description=open("README.rst").read(),
    author="Trevor Bramwell",
    author_email="trevor@bramwell.net",
    url="https://github.com/bramwelt/escape",
    packages=find_packages(),
)
