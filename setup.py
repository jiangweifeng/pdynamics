import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdynamics",
    version="0.2.4",
    author="Weifeng Jiang",
    author_email="jiangweifeng@live.com",
    description="Python connector for Microsoft Dynamics 365, supports AD, IFD and Online",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiangweifeng/pdynamics",
    install_requires=[
        'requests>=2.0.0',
        'requests_ntlm>=1.1.0'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)