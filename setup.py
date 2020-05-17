from setuptools import setup


from pyemoji import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyemoji',
    version=__version__,
    author=__author__,
    author_email="ocordes@astro.uni-bonn.de",
    description="Python module to provide simple emojis as strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ocordes/python-simple-emoji.git",
    packages=['pyemoji'],
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
