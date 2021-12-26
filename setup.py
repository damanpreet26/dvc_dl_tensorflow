from setuptools import setup

with open("requirements.txt","r+") as f:
    long_desc = f.read()

setup(
    name="src",
    version="0.0.1",
    author="demon",
    description="A small package for dvc pipeline",
    long_description=long_desc,
    url="https://github.com/damanpreet26/dvc_dl_tensorflow",
    author_email="damanpreets26@gmail.com",
    package=["src"],
    license="GPU",
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "numpy",
        "matplotlib",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3"
    ]
)