from setuptools import setup, find_packages

setup(
    name='openalex_search',
    version='0.1.0',
    author='Dion Xia',
    author_email='yudiandx@andrew.cmu.edu',
    description='A tool to search and rank OpenAlex publications based on citations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dionxia/openalex_search',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'openalex-search=openalex_search.cli:main',
        ]
    }
)
