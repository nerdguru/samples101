import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samples101",
    version="0.0.1",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nerdguru/samples101",
    packages=setuptools.find_packages(),
    install_requires=[
       'pyfiglet',
       'requests'
    ],
)
