"""setup"""
import io

from setuptools import find_packages, setup


def read_file(filename):
    """read file content"""
    with io.open(filename, encoding="utf-8") as fp:
        return fp.read().strip()


def read_requirements(filename):
    """read requirements"""
    return [
        line.strip()
        for line in read_file(filename).splitlines()
        if not line.startswith("#")
    ]


setup(
    name="notify",
    version="0.1.0",
    description="Load settings in various ways for Python projects",
    long_description=read_file("README.md"),
    author="taicaile",
    url="https://github.com/taicaile/python-notify",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=read_requirements("requirements.txt"),
)
