python-package-boilerplate
==========================

Boilerplate for a Python Package

## Package

Basic structure of package is

```
├── README.md
├── packagename
│   ├── __init__.py
│   ├── packagename.py
│   └── version.py
├── pytest.ini
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── helpers
    │   ├── __init__.py
    │   └── my_helper.py
    ├── tests_helper.py
    └── unit
        ├── __init__.py
        ├── test_example.py
        └── test_version.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Setup

To set up your package, ensure you have the necessary files and directories as shown in the package structure above. Specifically, you'll need:

- `README.md`: This file.
- `packagename/`: Directory containing your package's main code.
- `tests/`: Directory containing your tests.

### Setup Commands

1. **Install the package:**
   ```
   pip install .
   ```

2. **Install the package in editable mode (for development):**
   ```
   pip install -e .
   ```

3. **Upload to PyPI:**
   ```
   python setup.py sdist
   twine upload dist/*
   ```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled with the pytest-cov plugin.

### Running Tests

Run your tests with:

```
pytest
```

in the root directory.

### Coverage

Coverage is run by default and is set in the `pytest.ini` file. To see an HTML output of coverage, open `htmlcov/index.html` after running the tests.

## Continuous Integration

### Travis CI

There is a `.travis.yml` file that is set up to run your tests for multiple Python versions. To enable Travis CI for your repository, follow these steps:

1. Sign in to [Travis CI](https://travis-ci.org) with your GitHub account.
2. Enable Travis CI for your repository.
3. Push your code to GitHub to trigger a build.

### GitHub Actions (Optional)

If you prefer GitHub Actions for CI, you can set it up with a `.github/workflows/ci.yml` file. Here’s a basic example:

```yaml
name: CI

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
      - name: Check out repository code
        uses: actions/checkout@v2

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: |
          pytest --cov=packagename

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v1
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
```

This will set up CI for multiple Python versions and upload the coverage report to Codecov.

## License

Specify your package's license. For example:

```
MIT License
```

## Contribution Guidelines

If you want others to contribute to your package, add contribution guidelines. For example:

- Fork the repository.
- Create a new branch (`git checkout -b feature-foo`).
- Commit your changes (`git commit -am 'Add feature foo'`).
- Push to the branch (`git push origin feature-foo`).
- Create a new Pull Request.

Feel free to customize this boilerplate according to your specific needs.
