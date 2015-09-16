from distutils.core import setup

setup(
    # Application name:
    name="sheetmusic",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Hakon Jensen",
    author_email="hakon@hokky.org",

    # Packages
    packages=["sheetmusic"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/hakonaj/sheetmusic/",

    #
    # license="LICENSE.txt",
    description="Manage and share sheet music",

    # long_description=open("README.txt").read(),


    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)
