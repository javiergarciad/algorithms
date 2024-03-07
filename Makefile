PYTHON_VERSION = 3.12
PY = python$(PYTHON_VERSION)
VENV = .venv
BIN=$(VENV)/bin


$(VENV): requirements.txt
	$(PY) -m venv $(VENV) && \
	$(BIN)/pip install --upgrade pip && \
	$(BIN)/pip install -r requirements.txt && \
	touch $(VENV)

.PHONY: format
format: $(VENV)
	. $(BIN)/activate && \
	$(BIN)/ruff check --line-length 120 --fix-only src && \
	$(BIN)/usort format src

.PHONY: lint
lint: $(VENV)
	. $(BIN)/activate && \
	$(BIN)/ruff lint --line-length 120 src && \
	$(BIN)/usort check src
