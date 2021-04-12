import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platypus-python",
    version="1.0.0",
    author="Wang Yihang",
    author_email="wangyihanger@gmail.com",
    description="Python SDK for reverse shell sessions manager - Platypus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WangYihang/Platypus-Python",
    packages=["platypus_python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Topic :: System :: Networking",
    ],
    python_requires='>=3.6',
    keywords='platypus, sdk, reverse shell',
    install_requires=["requests"],
)