"""Install arxiv.feedback."""

from setuptools import setup, find_packages


setup(
    name='arxiv-feedback',
    version='0.0.0',
    packages=[f'arxiv.{package}' for package
              in find_packages('arxiv', exclude=['*test*'])],
    zip_safe=False,
    install_requires=[
        'flask',
        'pytz',
        'typing-extensions'
    ],
    include_package_data=True
)
