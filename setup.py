from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="freezing-demo",
    version="0.0.1",
    description="A sample Python project to demo PyInstaller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samj1912/freezing-demo",
    author="Sambhav Kothari",
    author_email="sambhavs.email@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="freezing build tools packaging CI CD",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.6",
    install_requires=["Click==7.0", "Markdown==2.6.11", "py-gfm==0.1.4"],
    extras_require={},
    scripts=['md-viewer'],
    package_data={"mdviewer": ["*.css"]},
)
