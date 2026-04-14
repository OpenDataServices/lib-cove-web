from setuptools import setup, find_packages

install_requires = []

setup(
    name='libcoveweb',
    version='0.31.2',
    author='Open Data Services',
    author_email='code@opendataservices.coop',
    packages=find_packages(),
    package_data={
        'cove': [
            'fixtures/*',
            'locale/*/*/*.po',
            'locale/*/*/*.mo',
            'sass/*/*',
            'sass/*/*/*',
            'sass/*/*/*/*',
            'static/*/*',
            'static/*/*/*',
            'static/*/*/*/*',
            'templates/*'
        ]
    },
    scripts=['manage.py'],
    url='https://github.com/OpenDataServices/lib-cove-web',
    description='',
    classifiers=["License :: OSI Approved :: BSD License"],
    python_requires=">=3.8",
    install_requires=[
        "Django>=4.2,<5.3",
        "django-bootstrap3",
        "requests",
        "flattentool",
        "werkzeug",
        "libcove>=0.17.0",
    ],
    extras_require={
        'test': [
            "flake8",
            "pytest",
            "pytest-django",
            "pytest-cov",
            "pytest-localserver",
            "pytest-xdist",
            "coveralls",
            "selenium",
            "transifex-client",
            "libsass",
            "hypothesis",
        ],
    }
)
