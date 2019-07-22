import setuptools

setuptools.setup(
    name="samples101",
    version="0.0.6",
    description="A small example package",
    url="https://github.com/nerdguru/samples101",
    packages=setuptools.find_packages(),
    install_requires=[
       'pyfiglet',
       'requests'
    ],
)
