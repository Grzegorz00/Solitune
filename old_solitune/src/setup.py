import setuptools

with open("README.md") as buffer:
    long_description = buffer.read()

setuptools.setup(
    name="appTemp",
    version="0.4.3",
    author="Temp",
    author_email="temp@pjwstk.edu.pl",
    description="My app temp",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas==1.4.2"
    ],
    python_requires=">=3.6",
)
