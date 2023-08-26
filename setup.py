from setuptools import setup

setup(
    name="flaskdl",
    version="0.1",
    packages=["flaskdl"],
    install_requries=[
        "flask",
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
