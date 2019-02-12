import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

# calls setup() to install
setup(
    name="awlify",
    version="1.1.2",
    description="a simple utility to take in a sentence and "
                "output information about the AWL words in it",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lpmi-13/awlify-python",
    author="Adam Leskis",
    author_email="leskis@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=('tests',)),
    install_requires=["spacy>=2.0.16"],
)
