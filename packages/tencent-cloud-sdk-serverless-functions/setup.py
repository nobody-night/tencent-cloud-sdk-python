# setup is python-3.6 source file

# MIT License
# 
# Copyright (c) 2020 Tencent Cloud.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
Tencent Cloud SDK for Python Sub-Package installer
https://github.com/nobody-night/tencent-cloud-sdk-python
'''

import setuptools

setuptools.setup(
    name = 'tencent-cloud-sdk-serverless-functions',
    version = '0.1.1',
    packages = [
        'tencent.cloud.serverless.functions'
    ],
    keywords = 'tencent-cloud sdk-python',
    license = 'MIT License',
    author = 'Tencent Cloud',
    author_email = 'support@xiaoyy.org',
    description = (
        'Tencent Cloud SDK for Python components. '
        'This package is the core component of the '
        'Tencent Cloud SDK. Most Tencent Cloud SDK '
        'components depend on this package.'
    ),
    url = 'https://github.com/nobody-night/tencent-cloud-sdk-python',
    python_requires = '>=3.6',
    zip_safe = False,
    classifiers = (
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable'
    ),
    install_requires = [
        'tencent-cloud-sdk-core>=0.1.1'
    ]
)
