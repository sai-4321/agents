# Copilot / AI Agent Instructions for WeatherMapApi

Purpose
- This repo is a minimal Streamlit app that fetches OpenWeatherMap data and uses Google GenAI (Gemini) to produce clothing/skincare suggestions.

Big picture
- Single-entry app: [index.py](index.py) is the whole application. User input flows: sidebar text -> `api_data(city)` -> OpenWeatherMap JSON -> UI metrics -> `llm_call(data)` -> LLM-generated suggestions displayed in the main view.
- External integrations: OpenWeatherMap REST API (requests) and Google GenAI via `google.genai.Client`.

What an agent should know (concrete, discoverable facts)
- Entrypoint: run the app with Streamlit: activate the virtualenv then `streamlit run index.py`.
- Key functions: `api_data(city)` (requests GET to OpenWeatherMap) and `llm_call(data)` (calls `genai.Client().models.generate_content`). See examples in [index.py](index.py#L1-L120).
- Secrets: API keys are currently hard-coded in `index.py`. Treat them as secrets — do not commit new secrets. Prefer replacing with environment variables (e.g. `os.getenv('OPENWEATHER_API_KEY')` / `GOOGLE_API_KEY`).
- Dependencies: obvious packages used are `streamlit`, `requests`, and the Google GenAI client under `google.genai` (check `myenv/Lib/site-packages` for precise package names/versions).

Run / debug workflow
- Activate venv (PowerShell):

  ```powershell
  .\myenv\Scripts\Activate.ps1
  ```

- Run Streamlit locally:

  ```powershell
  streamlit run index.py
  ```

- Quick debug tips:
  - Use `st.write()` or `st.json()` in `index.py` to inspect runtime values (e.g., `data` from `api_data`).
  - The app is single-file; small changes can be tested quickly by saving and reloading Streamlit.

Project-specific conventions and notes
- Minimal / single-file app: changes should preserve the simple linear flow unless extracting modules for testability.
- LLM usage pattern: `client.models.generate_content(model="gemini-3-flash-preview", contents=...)` — keep the same shape when editing prompts; examples live in `llm_call` in [index.py](index.py#L12-L60).
- UI layout: the app uses `st.sidebar` for input and two-column metrics (`st.columns(2)`) for temperature and humidity — keep screens small and readable on desktop.

Safety and operational cautions
- Do not commit API keys. If you find keys in the repo, flag them and rotate them with the owner.
- Limit model calls while developing (they may incur costs). Cache responses locally when iterating on prompt text.

Editing guidance for agents
- When refactoring, extract helper functions into a new module (e.g., `weather/api.py`) and update imports in `index.py`.
- Replace hard-coded secrets with `os.environ` reads and document required env vars in README or a `requirements.txt` (if you add one).
- Keep Streamlit control flow unchanged: avoid moving IO into background threads unless adding explicit async handling.

Where to look next
- Main app: [index.py](index.py)
- Virtualenv / installed packages: `myenv/Lib/site-packages`

If anything here is unclear or you want a different level of detail (examples for replacing keys, adding CI checks, or extracting modules), tell me which section to expand.
