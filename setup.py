from setuptools import setup

setup (
    name="fsw-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "fsw stands for Flask Starter Website. These are the core packages for this app.",
    packages=['fsw_config','fsw_models'],
    python_requires=">=3.10",
    )