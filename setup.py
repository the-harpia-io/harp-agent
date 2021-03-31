from setuptools import setup, find_packages
import os
import pwd
import grp
import sys
from setuptools import Command
from setuptools.command.install import install

# SERVICE_NAME = 'harp-agent'
# SERVICE_NAME_NORMALIZED = SERVICE_NAME.replace('-', '_')

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of Harp Agent requires Python {}.{}, but you're trying to
install it on Python {}.{}.
Please install Python version >=3.7
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


# def change_fcgi_permissions(files=None, folders=None):
#     if files:
#         for file in files:
#             os.chmod(file, 0o755)
#     if folders:
#         for folder in folders:
#             os.chmod(folder, 0o655)


# def create_folders():
#     directories = ['/etc/harp-gate-client', '/var/log/harp-gate-client']
#     uid = pwd.getpwnam("root").pw_uid
#     gid = grp.getgrnam("root").gr_gid
#     for directory in directories:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#             os.chown(directory, uid, gid)


# class CustomInstallCommand(Command):
#     user_options = []
#
#     def initialize_options(self):
#         """Abstract method that is required to be overwritten"""
#
#     def finalize_options(self):
#         """Abstract method that is required to be overwritten"""
#
#     def run(self):
#         create_folders()
#         # change_fcgi_permissions([],
#         #                         [f'/opt/fcgi/'])

# class CustomInstallCommand(install):
#     """Customized setuptools install command - prints a friendly greeting."""
#     def run(self):
#         print("Hello, developer, how are you? :)")
#         install.run(self)


tests_require = ['test'],


setup(
    name='harp-agent',
    python_requires='>3.7.0',
    version='1.0.0',
    description="Harp Agent",
    url='',
    include_package_data=True,
    author='',
    author_email='',
    classifiers=[
    ],
    keywords=[],
    packages=find_packages(),
    install_requires=requirements,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'harp-agent = harp_agent.app:main',
            'harp-agent-add = cmd_command.agent_configuration:agent_add',
            'harp-agent-update = cmd_command.agent_configuration:agent_update',
            'harp-agent-delete = cmd_command.agent_configuration:agent_delete',
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
