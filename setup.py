import sys

from setuptools import setup, find_packages

install_requires=[]

setup(
    name='FPMB',
    version='0.1.0',
    url='http://github.com/bukka/fpmb/',
    license='BSD',
    author='Jakub Zelenka',
    author_email='bukka@php.net',
    description='FPM Benchmark',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    entry_points = {
        'console_scripts': [
            'fpmb = fpmb.fpmb:main',
        ]
    }
)
