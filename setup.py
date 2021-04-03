from setuptools import setup, find_packages


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
    data_files=[]
)
