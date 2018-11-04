from setuptools import setup, find_packages

setup(
    name="slips",
    version="0.1",
    packages=find_packages(),
    scripts=['slips.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Thomas Kiley",
    author_email="thk123@github.com",
    description="A tool to help novice and young Python developers fix common errors in their code",
    license="Apache-2.0",
    keywords="lint parsing friendly beginner slipups common errors compiler",
    url="https://github.com/thk123/slips/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://github.com/thk123/slips/",
    }

    # could also include long_description, download_url, classifiers, etc.
)
