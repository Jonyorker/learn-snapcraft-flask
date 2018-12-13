from setuptools import setup, find_packages

setup(
    name="Hello World",
    version="1.0.0",
    long_description=__doc__,
    # packages=["hello"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["Flask>=0.2"],
)
