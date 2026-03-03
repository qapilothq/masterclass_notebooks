# Masterclass Notebook

Generate and evaluate **BDD-style (Given/When/Then)** mobile app test cases using an LLM. The project uses OpenAI to produce test scenarios and an LLM-as-judge to score their quality.

## What’s in this repo

| File | Description |
|------|-------------|
| **test_case_generation.ipynb** | Generates BDD test cases in three ways: from app name only, from app name + context, and from an app screen graph. |
| **llm_as_judge.ipynb** | Evaluates the three generated test sets with a rubric and returns scores plus a recommendation. |
| **requirements.txt** | Python dependencies (`ipykernel`, `openai`, `python-dotenv`). |

## Setup

### 1. Python environment

**Option A: Virtual environment (recommended)**

```bash
cd masterclass_notebook
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Option B: Use the existing `.venv`**

If `.venv` already exists, activate it and ensure dependencies are installed:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. API key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

Optional (defaults to `gpt-4o-mini` if unset):

```env
OPENAI_MODEL=gpt-4o
```

Both notebooks read `OPENAI_API_KEY` (and optionally `OPENAI_MODEL`) from `.env`.

### 3. Jupyter kernel (for running in VS Code / Cursor)

To register the venv as a kernel:

```bash
.venv/bin/python -m ipykernel install --user --name=masterclass_notebook --display-name="Python (masterclass_notebook)"
```

Then in your editor, select the interpreter or kernel **Python (masterclass_notebook)** (or the `.venv` interpreter) before running the notebooks.

## Usage

1. **Run `test_case_generation.ipynb`**  
   - Set `APP_NAME`, `APP_CONTEXT`, and optionally `APP_PACKAGE_NAME` in the first cell.  
   - Run all cells. This produces:
     - `test_cases_simple/` — from app name only  
     - `test_cases_with_context/` — from app name + context  
     - `test_cases_from_graph/` — from screen graph (uses `app_screen_graph.json` if present, otherwise a demo graph)

2. **Run `llm_as_judge.ipynb`**  
   - Uses the same `APP_NAME` and `APP_CONTEXT` and reads the JSON files from the three output folders.  
   - Run all cells to get scores (1–5 per criterion), summaries, and a recommendation.

## Output layout

After running the generation notebook you’ll have:

- `test_cases_simple/<AppName>_test_cases.json`
- `test_cases_with_context/<AppName>_test_cases.json`
- `test_cases_from_graph/<AppName>_graph_test_cases.json`

The judge notebook loads these paths automatically based on `APP_NAME`.

## Optional: screen graph

For the “from graph” flow, put an `app_screen_graph.json` in the project root. Example shape:

```json
{
  "nodes": [
    {"id": "home", "label": "Home Screen", "description": "..."},
    {"id": "login", "label": "Login Screen", "description": "..."}
  ],
  "edges": [
    {"source": "splash", "target": "login", "action": "auto_navigate"},
    {"source": "login", "target": "home", "action": "tap_login"}
  ]
}
```

If the file is missing, the notebook falls back to a small demo graph.

## Requirements

- Python 3.10+
- OpenAI API key

See `requirements.txt` for Python packages.
