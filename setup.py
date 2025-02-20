from setuptools import setup, find_packages

setup(
    name="p4print",  # ✅ Change to your new package name
    version="0.2.1",  # Increment the version to avoid PyPI duplication issues
    packages=find_packages(),
    description="A simple package to use 'p()' instead of 'print()'",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ashish Kumar",
    author_email="ashish.jnu@outlook.com",
    url="https://github.com/AshishKumarCS/p4print",  # ✅ Update the GitHub repo link
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
