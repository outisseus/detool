PYTHON ?= python3
PYCACHE ?= /private/tmp/detool-pycache

.PHONY: setup test check example

setup:
	$(PYTHON) -m venv .venv
	.venv/bin/python -m pip install -e .

test:
	PYTHONPYCACHEPREFIX=$(PYCACHE) PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v

check:
	$(PYTHON) -m json.tool schemas/capability.json >/dev/null
	$(PYTHON) -m json.tool schemas/access-decision.json >/dev/null
	$(PYTHON) -m json.tool schemas/usage-proof.json >/dev/null
	PYTHONPATH=src $(PYTHON) -m detool validate examples/synthetic-capability.json

example:
	PYTHONPATH=src $(PYTHON) -m detool proof examples/synthetic-capability.json

