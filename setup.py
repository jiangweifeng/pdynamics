import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdynamics-jiangweifeng",
    version="0.1.5",
    author="Weifeng Jiang",
    author_email="jiangweifeng@live.com",
    description="Python connector for Microsoft Dynamics 365, supports AD, IFD and Online",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiangweifeng/pdynamics",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'requests_ntlm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)