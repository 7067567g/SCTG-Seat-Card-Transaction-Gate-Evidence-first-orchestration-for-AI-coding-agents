.RECIPEPREFIX = >
PYTHON ?= python3

.PHONY: check test demo clean

check:
> $(PYTHON) scripts/check_repo.py
> $(PYTHON) -m compileall -q kit scripts tests examples

test: check
> $(PYTHON) -m pytest -q

demo:
> $(PYTHON) examples/minimal-run/run_demo.py

clean:
> find . -name '__pycache__' -type d -prune -exec rm -rf {} +
> find . -name '*.pyc' -delete
> rm -rf examples/minimal-run/_run examples/minimal-run/work
