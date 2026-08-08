# AI Recipe Generator (Streamlit App)

A simple Streamlit app that generates a recipe from your ingredients, cuisine, and
dietary restrictions using the Google Gemini API.

## Prerequisites

- Python 3.9+
- A Google Gemini API key (from [Google AI Studio](https://aistudio.google.com/apikey))

## Setup

1. From the project root, install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Make sure the project root `.env` file has your API key set:

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Run the app

From the project root:

```bash
streamlit run recipe_generator/streamlit_app.py
```

This starts a local web server and prints a URL, typically:

```
Local URL: http://localhost:8501
```

Open that URL in your browser, enter your ingredients (comma separated), cuisine,
and dietary restrictions, then click **Generate Recipe**.

By default Streamlit runs in the foreground and opens a browser tab automatically.
To run it headless (no auto-opened browser tab, useful for background/remote runs):

```bash
streamlit run recipe_generator/streamlit_app.py --server.headless true
```

## Stop the app

- If running in the foreground: press `Ctrl+C` in the terminal where it's running.
- If running in the background: find and stop the process.

  ```bash
  # Windows (PowerShell)
  Get-Process -Name streamlit | Stop-Process

  # or find the process on the port and kill it
  netstat -ano | findstr :8501
  taskkill /PID <pid> /F
  ```

## Restart the app

Stop it (see above), then run the same command again:

```bash
streamlit run recipe_generator/streamlit_app.py
```

If you changed the port or it's still in use, specify a different port:

```bash
streamlit run recipe_generator/streamlit_app.py --server.port 8502
```

## Files

- `streamlit_app.py` — the Streamlit web app
- `recipe_generator.py` — CLI version of the same recipe generator
