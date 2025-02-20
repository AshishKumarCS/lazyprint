from setuptools import setup, find_packages

setup(
    name="lazyprint",  # Package name
    version="0.1",  # Initial version
    packages=find_packages(),
    description="I need to test output of programs many times. And, writing print many times make me slow. So, here is a simple package to use 'p()' instead of 'print()'",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ashish Kumar",
    author_email="ashish.jnu@outlook.com",
    url="https://github.com/AshishKumarCS/lazyprint",  # GitHub repo
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
