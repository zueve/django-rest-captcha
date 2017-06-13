from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Operating System :: OS Independent',
    'Topic :: System :: Networking',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Framework :: Django',
    'Framework :: django-rest-framework'
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
]

dev_require = [
    'ipython',
]

tests_require = [
    'tox',
    'six',
]

install_requires = [
    'djangorestframework>3.5.0',
    'django',
    'Pillow==4.1.1',
]

entry_points = {
}

setup(
    author='Evgeny Zuev',
    author_email='zuevesn@gmail.com',
    name='django-rest-captcha',
    description='Simple captha for django-rest-framework',
    version='0.0.4',
    url='https://github.com/zueve/django-rest-captcha',
    platforms=['OS Independent'],
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'dev': dev_require,
    },
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
    zip_safe=False,
    test_suite='',
)
