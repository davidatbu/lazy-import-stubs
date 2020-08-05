"""Package setup"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lazy-import-stubs",
    version="0.1",
    author="David Assefa Tofu",
    description="incomplete stubs for lazy-import.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["lazy-import-stubs"],
    python_requires=">=3.6",
    install_requires=["lazy-import==0.2.2", "typing_extensions"],
    package_data={"": ["*.pyi", "py.typed"]},
    extras_require={"dev": ["black", "mypy"]},
    classifiers=[  # classifiers can be found here: https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Typing :: Typed",
    ],
    zip_safe=False,
)
