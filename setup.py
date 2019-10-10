import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystackpath",
    version="0.0.2",
    author="Sandro Modarelli",
    author_email="sandro.modarelli@namecheap.com",
    description="A package to interact with StackPath",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NCCloud/pystackpath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries"
    ],
    keywords=[
        "stackpath",
        "cdn",
        "waf",
        "proxy",
        "kubernetes"
    ]
)