try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ""

setup(
    name='youtube-python-async',
    version='1.0.1',
    description='Python Youtube Data API v3 - Asynchronous',
    long_description=long_description,
    url='https://github.com/economy/youtube-python-async',
    author='economy',
    author_email='the.economy@gmail.com',
    license='GPL',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords="youtube data api python v3 async",
    packages=['youtube_async']
)
