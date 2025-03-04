from setuptools import setup, Extension, find_packages

# Define the extension module.
ext_modules = [
    Extension(
        "neatipy_c",  # Name of the extension module.
        sources=["neatipy/c/dataframe_formatter.c"],
        extra_compile_args=["-Ofast", "-march=native", "-funroll-loops"],
    )
]

# Read the long description from the README if you want.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="neatipy",
    version="0.1.0",
    description="Python object formatting and printing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vilppu Tiilikainen",
    author_email="vilppu.tiilikainen123@gmail.com",
    license="MIT",
    packages=find_packages(),
    ext_modules=ext_modules,
    install_requires=["numpy>=2.2.0", "pandas>=2.2.0"],
)
