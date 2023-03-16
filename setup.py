from setuptools import setup, find_packages

install_requires = []

setup(
    name='libcoveweb',
    version='0.27.0',
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
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    ],
    python_requires=">=3.7",
    install_requires=[
        "Django>=2.2",
        "django-bootstrap3",
        "requests",
        "django-environ",
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
