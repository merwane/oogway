import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="oogway",
        version="1.0.0",
        author="Merwane Drai",
        author_email="merwane@6conf.com",
        description="A simple, yet secure Bitcoin library",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/merwane/oogway",
        download_url = "https://github.com/merwane/oogway",
        license='MIT',
        keywords={
            "bitcoin",
            "bitcoin-sdk",
            "bitcoin-wallet",
            "bitcoin-cli"
            },
        classifiers=(
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
            ),
        install_requires=("ecdsa", "Click"),
        tests_require=["pytest"],
        packages = setuptools.find_packages(),
        entry_points='''
            [console_scripts]
            oogway=oogway.cli.cli:cli
        '''
        )
