# TODO
python setup.py sdist; export PYPI_USERNAME=the-harpia-io; export PYPI_PASSWORD=75Hu8x7faS; .circleci/upload-project.sh;  rm -r harp_agent.egg-info; rm -r dist

https://www.nylas.com/blog/packaging-deploying-python/

sudo apt-get install debhelper dh-virtualenv

# Create virtual env
sudo apt install python3.7-venv
python3.7 -m venv py37-venv
source py37-venv/bin/activate

https://opensource.com/article/20/4/package-python-applications-linux
https://mentors.debian.net/intro-maintainers/