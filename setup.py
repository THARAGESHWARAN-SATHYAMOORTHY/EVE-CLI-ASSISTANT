from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="EVE-CLI-ASSISTANT",
    version="0.1",
    author="Varun Suresh",
    description="EVE is a cli tool.",
    long_description="This is EVE, a command line based tool to help automate some processes and speeden up things.",
    url="https://github.com/VaryV/EVE-CLI-ASSISTANT",
    keywords=[
        "eve",
        "cli tool",
        "python cli tool",
        "eve cli tool",
        "eve command line tool",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        eve = eve.cli:cli
    """,
)
