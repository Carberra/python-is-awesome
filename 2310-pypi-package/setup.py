import pathlib

import setuptools

setuptools.setup(
    name="carberra",
    version="0.2.0",
    description="Brief description",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://carberra.xyz",
    author="Ethan Henderson",
    author_email="carberra.business@gmail.com",
    license="The Unlicense",
    project_urls={
        "Documentation": "https://carberra.xyz/docs",
        "Source": "https://github.com/carberra/pypi-tutorial",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10,<3.12",
    # install_requires=["requests", "pandas>=2.0"],
    # extras_require={
    #     "excel": ["openpyxl"],
    # },
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["carberra = carberra.cli:main"]},
)
