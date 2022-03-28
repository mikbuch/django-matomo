import os

from setuptools import setup, find_packages

setup(
    name='django-matomo',
    version='0.1',
    description='A simple app to add the Piwik JS tracking code to your template.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Raphael Jasjukaitis',
    author_email='webmaster@raphaa.de',
    url='https://github.com/raphaa/django-piwik',
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
