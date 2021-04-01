from setuptools import setup, find_packages
# import sys
# import subprocess
# import setuptools

# CURRENT_PYTHON = sys.version_info[:2]
# REQUIRED_PYTHON = (3, 7)
#
# if CURRENT_PYTHON < REQUIRED_PYTHON:
#     sys.stderr.write("""
# ==========================
# Unsupported Python version
# ==========================
# This version of Harp Agent requires Python {}.{}, but you're trying to
# install it on Python {}.{}.
# Please install Python version >=3.7
# """.format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
#     sys.exit(1)


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='harp-agent',
    python_requires='>3.7.0',
    version='1.0.4',
    description="Harp Agent",
    url='',
    include_package_data=True,
    author='harpia',
    author_email='the.harpia.io@gmail.com',
    maintainer='harpia',
    maintainer_email='the.harpia.io@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[],
    packages=find_packages(),
    install_requires=requirements,
    tests_require=[],
    entry_points={
        'console_scripts': [
            'harp-agent = harp_agent.app:main',
        ]
    },
    zip_safe=False,
    cmdclass={},
    data_files=[
        ('/etc/init.d', [
            'data/init-script/harp-agent'
        ])
    ]
)
