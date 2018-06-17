# sgcharts-timex

Datetime utilities in python3

## Usage 

Add this library as a dependency in `setuptools`.

Example `setup.py`

```python
install_requires=[
    'sgcharts-timex',
    ...
],
dependency_links=[
    'git+https://github.com/seahrh/sgcharts-timex.git@master#egg=sgcharts-timex-1.0.0'
]
```

You must specify the version at the *end* of the string in `dependency-links`.

Then run `pip install` in your project's virtual environment.

```
pip install --process-dependency-links git+https://github.com/seahrh/sgcharts-timex.git
```
