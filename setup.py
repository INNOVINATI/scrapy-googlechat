from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='scrapy-googlechat',
    version='1.1',
    description='Send crawl reports from Scrapy spiders to Google Chat',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/innovinati/scrapy-googlechat',
    author='Maximilian Wolf',
    author_email='maximilian.wolf@innovinati.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='scrapy, google chat, bot',
    py_modules=['scrapy_google_chat'],
    python_requires='>=3.5, <4',
    install_requires=['scrapy'],
    project_urls={
        'Bug Reports': 'https://github.com/innovinati/scrapy-googlechat/issues',
        'Source': 'https://github.com/innovinati/scrapy-googlechat/',
    },
)