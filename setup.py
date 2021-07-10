import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ut61e-DM",  # Replace with your own username
    version="0.0.1",
    author="Dmitry Melnichansky",
    author_email="iosaaris@gmail.com",
    description="Python library for reading data from UNI-T UT61E DMM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natecostello/ut61e_py",
    project_urls={
        "Bug Tracker": "https://github.com/natecostello/ut61e_py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=[''],
    python_requires=">=3.0",
    install_requires=[
        "pyserial>=3.3", #active release when initially this project was initially commited 
        ]
)