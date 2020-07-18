with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-zeerm
    version="0.0.1",
    author="Maarten Zeer",
    author_email="m.zeer@cargofit.nl",
    description="A package with CoDrone code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ms233r/CoDrone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)