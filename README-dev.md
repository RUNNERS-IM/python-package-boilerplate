# Developer Guide

This guide is for developers contributing to the library.

## Installation

To set up the development environment, follow these steps:

Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

Ensure all tests pass before making any changes. To run tests, use:

```bash
pytest
```


## Environment Variables
Create a .env file in the root directory with the following content:

```plaintext
KEY=VALUE
```

## Building the Package
To build the package, update the version in setup.cfg:
```ini
[metadata]
name = python-package-boilerplate
version = x.x.x
```

Then, build the package:
```bash
python setup.py sdist bdist_wheel
```

## Deploying the Package
To deploy the package to PyPI, use Twine:
```bash
twine upload --verbose dist/python-package-boilerplate-x.x.x.tar.gz
```
Ensure you have the necessary permissions to upload to the PyPI repository.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch (feature/your-feature-name). 
3. Commit your changes with descriptive commit messages. 
4. Push to the branch. 
5. Create a pull request.

## Code Style
Follow PEP 8 for Python code style. Use tools like flake8 for linting and black for code formatting.

## Contact
For any questions or support, please contact dev@runners.im.

