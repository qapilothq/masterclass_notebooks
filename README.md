# BDD Test Case Generation & LLM-as-Judge

Generate BDD (Given/When/Then) test cases for mobile apps using an LLM, then evaluate their quality with an LLM judge. Three levels of context are compared to show how richer input produces better tests.

## Notebooks

| Notebook | Description |
|---|---|
| `test_case_generation-BASIC.ipynb` | Starter template — fill in your app details |
| `test_case_generation-ADVANCED.ipynb` | Complete example using booking.com |
| `llm_as_judge-BASIC.ipynb` | Evaluation template — define your rubric |
| `llm_as_judge-ADVANCED.ipynb` | Complete evaluator with a 6-criterion weighted rubric |

## How It Works

Test cases are generated three ways, each producing progressively better results:

1. **Simple** — app name + basic description → saves to `test_cases_simple/`
2. **With context** — app name + description + screenshots → saves to `test_cases_with_context/`
3. **From graph** — app name + context + screen graph JSON + screenshots → saves to `test_cases_from_graph/`

The LLM judge then scores all three sets on BDD structure, domain relevance, coverage, clarity, scenario quality, and traceability (1–5 scale).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your-key-here
OPENAI_MODEL=gpt-4.1           # optional, defaults to gpt-4.1
```

Open the notebooks and select the `.venv` kernel.

## Capturing Screenshots (optional)

Screenshots placed in `screenshots/` are automatically included in generation modes 2 and 3.

To capture from a connected Android device via ADB:

```bash
python adb_screenshot.py                   # auto-named with timestamp
python adb_screenshot.py --name login.png  # custom filename
```

Requires ADB in PATH and USB debugging enabled on the device.

## App Graph (optional)

Place a JSON file describing your app's screen graph at `graphs/MY_APP_graph.json`. Any structure works — nodes/edges, adjacency lists, etc. The graph is stringified and included in the prompt for mode 3 generation.
