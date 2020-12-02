# coding=utf-8
"""
Setup for Fiducial Registration Educational Demonstration
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgeryfredmatplotlib',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='FRED provides an interactive demonstration of fiducial based registration for teaching purposes',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/UCL/scikit-surgeryfredmatplotlib',
    author='Stephen Thompson',
    author_email='s.thompson@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
            'numpy',
            'matplotlib',
            'scikit-surgeryfred',
            'ipykernel',
            'nbsphinx',
    ],

    entry_points={
        'console_scripts': [
            'sksurgeryfredmatplotlib=sksurgeryfredmatplotlib.__main__:main',
            'sksurgeryfredmatplotlib_plotter=sksurgeryfredmatplotlib.ui.sksurgeryfred_plotter_command_line:main',
            'sksurgeryfredmatplotlib_game=sksurgeryfredmatplotlib.ui.sksurgeryfred_game_command_line:main',
        ],
    },
)
