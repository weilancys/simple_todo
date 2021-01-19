from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = 'simple-todo',
    version = "0.0.1",
    author="lbcoder",
    author_email="lbcoder@hotmail.com",
    description="A simple todo web app",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/weilancys/simple_todo",
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        "flask",
        "flask-sqlalchemy",
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)