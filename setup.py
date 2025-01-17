from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="asteroid",
    version="0.1",
    author="University of Rhode Island",
    author_email="lutzhamel@uri.edu",
    description="A pattern-matching oriented programming language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lutzhamel/asteroid",
    packages=find_packages(),
    package_data={"asteroid": ["modules/*"]},
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "asteroid = asteroid:main",
        ],
    },
)
