import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdynamics",
    version="0.2.2",
    author="Weifeng Jiang",
    author_email="jiangweifeng@live.com",
    description="Python connector for Microsoft Dynamics 365, supports AD, IFD and Online",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiangweifeng/pdynamics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)