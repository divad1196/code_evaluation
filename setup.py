import setuptools

setuptools.setup(
    name="code_evaluation",
    version="0.1",
    author="Gallay David",
    author_email="davidtennis96@hotmail.com",
    description="A module to provide safer code evaluation and utilities",
    setup_requires=['setuptools-markdown'],
    long_description_content_type="text/markdown",
    long_description_markdown_filename='README.md',
    url="https://github.com/divad1196/code_evaluation",
    packages=setuptools.find_packages(),
    # install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)