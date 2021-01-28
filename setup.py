from setuptools import setup

setup(
    name='ae_python',
    version='1.0.0',
    author='Kalle Bracht',
    author_email='kalle.bracht@picoballoon.org',
    packages=["ae_python"],
    url="https://kalbra.github.io/after-effects-python/index.html",
    license='LICENSE',
    description='Create After Effects scripts in Python.',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "colour",
        "secrets",
    ],
)