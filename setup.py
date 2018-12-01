from setuptools import setup, find_packages
__version__ = '2.0.0'
setup(
    name="sgcharts.timex",
    version=__version__,
    python_requires='>=3.6.0',
    install_requires=[],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    description='Datetime utilities in python3',
    license='MIT',
    author='sgcharts',
    author_email='admin@sgcharts.com',
    url='https://github.com/seahrh/sgcharts.timex'
)
