from setuptools import setup

setup(
    name='my-python-package',
    version='0.0.1',    
    description='A example Python package',
    url='https://github.com/dexterdmonkey/my-python-package.git',
    author='Dexter DMonkey',
    author_email='mail@mail',
    license='BSD 2-clause',
    packages=['example_package'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)