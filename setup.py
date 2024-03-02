from setuptools import setup, find_packages

setup(
    name='salgorithm',
    version='0.0.1',
    description="让算法变得简单一点",
    long_description=open('./README.md').read(),
    include_package_data=True,
    author='SoulCodingYanhun',
    author_email='souls2906@gmail.com',
    maintainer='SoulCodingYanhun',
    maintainer_email='souls2906@gmail.com',
    license='MIT License',
    url='https://github.com/SoulCodingYanhun/salgorithm',  # 替换为您的GitHub仓库链接
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
    install_requires=[''],  # 添加您的依赖项
)
