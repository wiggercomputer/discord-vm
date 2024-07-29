from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="discord-vm",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dvm=dvm.dvm:main",
        ],
    },
    author="wiggercomputer",
    author_email="obama@wigger.gay",
    description="Send discord voice messages over the api",
    license="MIT",
    keywords="discord voice message",
    url="https://github.com/gnomegl/discord-vm",
    python_requires=">=3.6",
)
