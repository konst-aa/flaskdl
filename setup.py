from setuptools import setup, find_packages

setup(
    name="flaskdl",
    version="0.1",
    packages=find_packages(),
    install_requries=[
        "setuptools",
        "flask>=0.2",
        "asgiref",
        "youtube-dl",
    ],
    author="Dmytro Tsapiv, Konstantin Astafurov",
    author_email="konstantin.astafurov@gmail.com",
    description="Flask extension for downloading youtube videos.",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/konst-aa/flaskdl",
    python_requires=">=3.10",
)
