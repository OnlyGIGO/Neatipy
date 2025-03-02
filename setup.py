import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="Neatipy",
    version="0.1.0",
    author="Vilppu Tiilikainen",
    author_email="vilppu.tiilikainen123@gmail.com",
    description="Python object formatting and printing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OnlyGIGO/Neatipy",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License", 
    ],
    python_requires=">=3.10",
    install_requires=[
       "numpy>2.2",
       "pandas>2.2"
    ],
)
