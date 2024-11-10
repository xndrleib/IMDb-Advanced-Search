from setuptools import setup, find_packages

setup(
    name='imdb_search_filters',  # Name of your package
    version='0.1',               # Package version
    packages=find_packages(),    # Automatically find and include all packages
    install_requires=[           # List of dependencies your project needs
        # Example dependencies:
        # 'requests', 
        # 'beautifulsoup4', 
        # 'lxml'
    ],
    classifiers=[        
    ],
    author='Your Name',          # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A Python package for building and filtering IMDb search URLs based on various criteria.',
    # long_description=open('README.md').read(),  # Read your README file for long description
    # long_description_content_type='text/markdown',
    url='https://github.com/yourusername/imdb_search_filters',  # Replace with your GitHub repository URL
    project_urls={              # Optional: Add links to related resources
        # 'Documentation': 'https://github.com/yourusername/imdb_search_filters/wiki',
        # 'Source': 'https://github.com/yourusername/imdb_search_filters',
    },
    license='MIT',              # Replace with your license type
)
