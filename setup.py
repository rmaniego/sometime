import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'sometime',
    packages = ["sometime"],
    version = '1.0.0',
    license='MIT',
    description = 'Get timestamp, formatted date, and perform date/time operations.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/sometime',
    download_url = 'https://github.com/rmaniego/sometime/archive/v1.0.tar.gz',
    keywords = ['DATETIME', 'TIME', 'TIMESTAMP'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)