import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystackpath",
    version="0.0.1",
    author="Sandro Modarelli",
    author_email="sandro.modarelli@namecheap.com",
    description="A package to interact with StackPath",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NCCloud/pystackpath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords=[
        'stackpath',
        'cdn',
        'waf',
        'proxy',
        'kubernetes',
    ]
)