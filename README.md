# datacamp-ai-associate
Code &amp; Documentation from DataCamp AI Associate Path for Developers

## Setup

1. Install the dependencies:

   ```bash
   pip install --user openai python-dotenv
   ```

2. Copy `.env.example` to `.env` and set your OpenAI API key:

   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

3. Run a script:

   ```bash
   python openai_intro/basic_connection.py
   ```

## Project structure

- `openai_intro/basic_connection.py` — basic Chat Completions request. The client
  reads the API key from the `OPENAI_API_KEY` environment variable (loaded from
  `.env` via `python-dotenv`); no key is ever hardcoded in the source.
- `.env` — your real secrets. Gitignored, never committed.
- `.env.example` — template with dummy values only. Safe to commit.
- `.vscode/settings.json` — hides `.env` from the VS Code explorer, search, and
  quick-open so the key can't accidentally appear on a shared screen.

## Secret-handling policy

This repo is developed on a live stream, so keys must never be visible:

- **No hardcoded keys.** Scripts read `OPENAI_API_KEY` from the environment via
  `os.getenv()`; if it's missing they fail with an error message that does not
  include any secret value.
- **No logging of keys.** We never `print()`, log, or echo the API key or any
  other `.env` value — not in scripts, and not in terminal commands. Terminal
  checks only report *whether* a key is set (e.g. `True`/`False` or its length),
  never its contents. Commands like `cat .env`, `echo $OPENAI_API_KEY`, or
  `Get-Content .env` are off-limits while the screen is shared.
- **`.env` never leaves the machine.** It's listed in `.gitignore` and hidden
  from the VS Code UI. Edit it off-stream (e.g. `notepad .env` with screen
  share paused).
- **Rotate on exposure.** If a key ever does appear on screen or in a commit,
  revoke it immediately in the OpenAI dashboard and generate a new one.
