from setuptools import setup, find_packages

setup(
    name="package_name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 패키지 의존성을 여기에 추가하세요
    ],
    author="Your Name",
    author_email="dev@runners.im",
    description="A short description of the package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RUNNERS-IM/python-package-boilerplate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
