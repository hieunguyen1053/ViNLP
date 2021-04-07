import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="ViNLP",
    version="1.0.5",
    description="NLP package for Vietnamese",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hieunguyen1053/ViNLP",
    author="Hieu Nguyen",
    author_email="hieunguyen1053@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[
        "ViNLP",
        "ViNLP/datasets",
        "ViNLP/features",
        "ViNLP/models",
        "ViNLP/pipelines",
        "ViNLP/utils",
    ],
    include_package_data=True,
    install_requires=[
        "sklearn_crfsuite==0.3.6",
    ],
    entry_points={},
)