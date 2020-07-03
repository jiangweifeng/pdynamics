import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynamics365-jiangweifeng", # Replace with your own username
    version="0.1.3",
    author="Weifeng Jiang",
    author_email="jiangweifeng@live.com",
    description="Python connector for Microsoft Dynamics 365, supports AD, IFD and Online",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiangweifeng/pydynamics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)