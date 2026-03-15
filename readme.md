# Streamlit App

## Project Structure
```
streamlit-app/
├── app.py                  ← entire app lives here (Python only)
├── requirements.txt        ← dependencies
└── .streamlit/
    └── config.toml         ← dark theme config
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
# Opens automatically at http://localhost:8501
```

## Deploy to Streamlit Community Cloud (free)
1. Push this folder to a GitHub repository
2. Go to https://share.streamlit.io
3. Click **"New app"**
4. Select your repo, branch, and set **Main file path** to `app.py`
5. Click **Deploy** — live in ~60 seconds

## To change the options
Edit the `OPTIONS` list at the top of `app.py`:
```python
OPTIONS = [
    {"number": "01", "title": "Your Option", "desc": "Your description."},
    {"number": "02", "title": "Your Option", "desc": "Your description."},
]
```