from setuptools import setup

install_requires = []

with open('./requirements.in') as requirements_txt:
    requirements = requirements_txt.read().strip().splitlines()
    for requirement in requirements:
        if requirement.startswith('#'):
            continue
        elif requirement.startswith('-e '):
            install_requires.append(requirement.split('=')[1])
        else:
            install_requires.append(requirement)

setup(
    name='libcoveweb',
    version='0.11.0',
    author='Open Data Services',
    author_email='code@opendataservices.coop',
    packages=['cove', 'cove.input', 'cove.dataload', 'cove.lib'],
    scripts=['manage.py'],
    url='https://github.com/OpenDataServices/lib-cove-web',
    description='',
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    ],
    install_requires=install_requires,
)
