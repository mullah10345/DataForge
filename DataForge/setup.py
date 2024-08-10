from setuptools import setup, find_packages

setup(
    name='DataForge',
    version='0.1.0',
    description='A custom database engine with advanced features.',
    author='Daniel Kimeu',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/DataForge',  # Replace with your project URL
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
        'numpy',  # Example dependency
        'pandas',  # Example dependency
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'dataforge-cli=cli.dataforge_cli:main',  # Adjust to match your CLI entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
