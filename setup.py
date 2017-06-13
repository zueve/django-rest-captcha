from setuptools import setup

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Operating System :: OS Independent',
    'Topic :: System :: Networking',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Environment :: Console',
    'Intended Audience :: Developers',
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
    description='Simple captha for django rest framework',
    version='0.0.2',
    url='https://github.com/zueve/django-rest-captcha',
    platforms=['OS Independent'],
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'dev': dev_require,
    },
    package_dir={'rest_captcha': 'rest_captcha'},
    packages=['rest_captcha'],
    entry_points=entry_points,
    include_package_data=True,
    zip_safe=False,
    test_suite='',
)
