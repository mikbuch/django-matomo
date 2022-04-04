import os

from setuptools import setup, find_packages

setup(
    name='django-matomo',
    version='0.1.6',
    description='A simple app to add the Matomo JS tracking code to your template. Forked from `django-piwik`.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Mikolaj Buchwald',
    author_email='mikolaj.buchwald@gmail.com',
    url='https://github.com/mikbuch/django-matomo',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=['Django'],
)
