from setuptools import setup, find_packages

# Read the requirements from requirements.txt


def parse_requirements(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().splitlines()


setup(
    name="palindrome_project",
    version="0.1.0",
    description="A REST API to generate and retrieve palindrome or non-palindrome strings.",
    author="Daria S",
    packages=find_packages(),  # Include tests and all other packages
    include_package_data=True,
    python_requires=">=3.12",
    install_requires=parse_requirements("requirements.txt"),  # Dynamic requirement loading
    extras_require={
        "dev": [
            "pytest>=8.3.3",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "run-palindrome=app.app:main",
        ]
    },
)
