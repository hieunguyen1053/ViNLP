from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ViNLP",
    version="1.2.103",
    description="NLP package for Vietnamese",
    long_description=long_description,
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
        "ViNLP/pipeline",
        "ViNLP/utils",
    ],
    include_package_data=True,
    install_requires=[
        "sklearn_crfsuite==0.3.6",
    ],
    entry_points={},
)