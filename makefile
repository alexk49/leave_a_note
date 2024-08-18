export PYTHONPATH := $(shell pwd)

DEV_VENV=dev-venv
DEV_VENV_DIR=./.$(DEV_VENV)
DEV_PIP=$(DEV_VENV_DIR)/bin/pip

VENV_NAME?=venv
VENV_DIR?=./.$(VENV_NAME)
VENV_PIP=${VENV_DIR}/bin/pip

all: venv setup test
dev: dev_venv dev_setup test
dev_venv:
		 test -d $(DEV_VENV_DIR) || python3 -m venv $(DEV_VENV_DIR)
dev_setup: dev_venv
		$(DEV_PIP) install --upgrade pip
		$(DEV_PIP) install -r dev-requirements.txt
venv:
		 test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
setup: venv
		 $(VENV_PIP) install --upgrade pip
		 $(VENV_PIP) install -r requirements.txt

test: dev dev_setup
		$(DEV_VENV_DIR)/bin/python3 -m unittest discover -v
clean:
		rm -rf $(VENV_NAME)
		rm -rf $(DEV_VENV_DIR)
		# delete pycache files
		py3clean .
run: venv
	$(VENV_DIR)/bin/python3 leave_a_note/app.py

.PHONY: test setup clean venv dev dev_setup run
