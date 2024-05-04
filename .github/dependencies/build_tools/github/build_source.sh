#!/bin/bash

set -e
set -x

# Move up two levels to create the virtual
# environment outside of the source folder
# cd ../../

python -m venv build_env
source build_env/bin/activate

cd .github/dependencies/
pwd
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
cd /home/runner/work/PKScreener/PKScreener/
python3 -m pip install --upgrade pip
pip3 uninstall -y PKNSETools
pip3 uninstall -y PKDevTools
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
pip3 install ta-lib==0.4.28
pip3 install .
python -m pip install setuptools twine wheel build

# python3 setup.py clean build sdist bdist_wheel
python -m build --sdist

# Check whether the source distribution will render correctly
twine check dist/*.tar.gz