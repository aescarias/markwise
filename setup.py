from setuptools import setup

import re

with open('markwise/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

print(version)

requirements = []

with open("README.md", "r") as f:
    readme = f.read()

setup(name="markwise",
      packages=["markwise"],
      author='SnowballSH, Tekgar',
      version=version,
      description="A Python wrapper for Markdown",
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires=">=3.6",
      url="https://github.com/angelCarias/markwise",
      download_url="https://github.com/angelCarias/markwise/archive/v0.1.2.tar.gz"
      )
