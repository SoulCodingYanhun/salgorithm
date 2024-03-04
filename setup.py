from setuptools import setup, find_packages

# Load the README.md file for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='salgorithm',
    version='0.0.9',
    description="让算法变得简单一点",
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the content type as Markdown
    include_package_data=True,
    author='SoulCodingYanhun',
    author_email='souls2906@gmail.com',
    maintainer='SoulCodingYanhun',
    maintainer_email='souls2906@gmail.com',
    license='Apache License',
    url='https://github.com/SoulCodingYanhun/salgorithm',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
    install_requires=[''],  # Add your dependencies here
)
