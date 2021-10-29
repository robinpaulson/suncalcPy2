from setuptools import setup

setup(
    name='suncalcPy2',
    version='0.1.0',
    description='A lightweight module for calculating the location of celestial objects',
    url='https://github.com/robinpaulson/suncalcPy2',
    author='Robin Paulson',
    author_email='robin@bumblepuppy.org',
    license='MIT',
    data_files = [("", ["LICENSE"])],
    packages='suncalcPy2',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
