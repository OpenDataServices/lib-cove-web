from setuptools import setup, find_packages

install_requires = []

setup(
    name='libcoveweb',
    version='0.18.3',
    author='Open Data Services',
    author_email='code@opendataservices.coop',
    packages=find_packages(),
    package_data={
        'cove': [
            'fixtures/*',
            'locale/*/*/*.po',
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
    install_requires=[
        "Django<2.3",
        "django-bootstrap3",
        "django-debug-toolbar",
        "requests",
        "cached-property",
        "dealer",
        "django-environ",
        "zipp==1.2.0",
        "jsonschema",
        "jsonref",
        "json-merge-patch",
        "python-dateutil",
        "sentry-sdk",
        "strict-rfc3339",
        "rfc3987",
        "rfc6266",
        "xmltodict",
        # libcove deps on flatten-tool which pulls in openpyxl
        # which is only compatible with certain versions of python
        "openpyxl==2.6.4",
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
