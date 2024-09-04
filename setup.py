from setuptools import setup

setup(
    name='pacote_AndreCorrea',
    version='0.1.0',
    description='Uma descrição do meu pacote',
    author='AndreCorreaSantos',
    author_email='andrecs11@al.insper.edu.br',
    install_requires=[
        "requests==2.32.3"
    ],
    python_requires='>=3.8, <=3.12',
    platforms=['Windows', 'Linux', 'MacOS'],
    scripts=['scripts/hello.py'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)