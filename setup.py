#!/usr/bin/env python

from reviewboard.extensions.packaging import setup


PACKAGE = 'rbnicknameauth'
VERSION = '0.3'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Nickname-only authentication for Review Board',
    url='',
    author='Matthew N.',
    author_email='',
    maintainer='',
    maintainer_email='',
    packages=['rbnicknameauth'],
    install_requires=[
        'ReviewBoard>=1.8alpha0.dev',
    ],
    entry_points={
        'reviewboard.extensions': [
            'rbnicknameauth = rbnicknameauth.extension:RBNicknameAuthExtension',
        ],
    },
    package_data={
        'rbnicknameauth': [
            'static/css/*',
            'static/js/*',
        ]
    },
)
