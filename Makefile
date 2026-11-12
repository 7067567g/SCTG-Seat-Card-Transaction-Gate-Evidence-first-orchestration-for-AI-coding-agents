.RECIPEPREFIX = >
PYTHON ?= python3

.PHONY: check test demo lint typecheck coverage audit bench clean

check:
> $(PYTHON) scripts/check_repo.py
> $(PYTHON) -m compileall -q kit scripts tests examples

test: check
> $(PYTHON) -m pytest -q

demo:
> $(PYTHON) examples/minimal-run/run_demo.py

lint:
> $(PYTHON) -m ruff check kit scripts tests examples benchmarks

typecheck:
> $(PYTHON) -m mypy --ignore-missing-imports kit

coverage:
> $(PYTHON) -m pytest --cov=kit --cov-report=term-missing --cov-fail-under=45

audit:
> $(PYTHON) -m pip_audit -r requirements.txt

bench:
> $(PYTHON) benchmarks/bench_gates.py

clean:
> find . -name '__pycache__' -type d -prune -exec rm -rf {} +
> find . -name '*.pyc' -delete
> rm -rf examples/minimal-run/_run examples/minimal-run/work
