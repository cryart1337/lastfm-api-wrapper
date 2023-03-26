from setuptools import setup, find_packages

setup(
    name="lafmapi",
    version="0.1.0",
    description="Python wrapper for the Last.fm API",
    url="https://github.com/Gaming552/lastfm-api-wrapper",
    author="cryart",
    author_email="dunariibot@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="lastfm api wrapper",
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests"],
    python_requires=">=3.6",
)
