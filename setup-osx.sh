#!/usr/bin/env bash
set -e
PYTHON_VERSION=3.7.4
wget "https://www.python.org/ftp/python/${PYTHON_VERSION}/python-${PYTHON_VERSION}-macosx10.9.pkg"
sudo installer -pkg python-${PYTHON_VERSION}-macosx10.9.pkg -target /
sudo python3 -m ensurepip
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip setuptools wheel pyinstaller
