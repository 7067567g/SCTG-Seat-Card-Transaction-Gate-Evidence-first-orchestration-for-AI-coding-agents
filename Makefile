.RECIPEPREFIX = >
PYTHON ?= python3

.PHONY: check test demo clean

check:
> $(PYTHON) scripts/check_repo.py
> $(PYTHON) -m py_compile kit/sctg.py kit/gates/*.py scripts/check_repo.py examples/minimal-run/run_demo.py tests/test_public_repo.py

test: check
> $(PYTHON) -m pytest -q

demo:
> $(PYTHON) examples/minimal-run/run_demo.py

clean:
> find . -name '__pycache__' -type d -prune -exec rm -rf {} +
> find . -name '*.pyc' -delete
> rm -rf examples/minimal-run/_run examples/minimal-run/work
