# ResumEnhancer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)
![OpenAI](https://img.shields.io/badge/GPT--4o-OpenAI-green)
![RenderCV](https://img.shields.io/badge/RenderCV-LaTeX-orange)

A CLI + Streamlit app that uses GPT-4o to ATS-optimize a YAML resume against a job description, then renders the result to a polished LaTeX PDF via [RenderCV](https://docs.rendercv.com).

**Streamlit UI:**
- Paste a job description (or fetch from a LinkedIn URL)
- Upload your `resume.yaml`
- Click **Enhance Resume** → review + edit the output → click **Render to PDF** → download

**CLI (headless):**
```bash
python main.py resume.yaml
# paste job description at the prompt, press Enter twice
```

---

## Setup

### 1. Clone and install

```bash
git clone <repo-url> && cd ResumEnhancer
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set your API key

```bash
cp .env.example .env
# edit .env — add your OPENAI_API_KEY
```

Get a key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501).

---

## Project Structure

```
ResumEnhancer/
├── app.py               # Streamlit frontend
├── main.py              # CLI entry point
├── resume.py            # GPT-4o prompt template (YAML schema for RenderCV)
├── jobDescription.py    # LinkedIn job scraper (optional, requires RapidAPI key)
├── resume.yaml          # Example RenderCV resume — replace with your own
├── mycustomtheme/       # Custom RenderCV theme (LaTeX)
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## How It Works

1. **Job description** — paste directly or fetch from a LinkedIn URL via the RapidAPI LinkedIn scraper
2. **Resume input** — upload a `resume.yaml` in [RenderCV format](https://docs.rendercv.com/user_guide/structure_of_the_yaml_input_file/)
3. **GPT-4o prompt** — `resume.py` contains the full YAML schema with `design` and `locale_catalog` blocks so the model knows exactly what structure RenderCV expects
4. **YAML validation** — `yaml.safe_load()` runs before anything hits RenderCV to catch model errors early
5. **PDF rendering** — RenderCV compiles the YAML through LaTeX into a polished PDF using the custom theme

---

## LinkedIn URL Scraping (optional)

If you want to fetch job descriptions from LinkedIn URLs automatically:

1. Get a free key at [RapidAPI — LinkedIn API](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8)
2. Add `RAPIDAPI_KEY=your_key` to your `.env` file
3. In the Streamlit UI, select **Fetch from LinkedIn URL** and paste a URL:
   ```
   https://www.linkedin.com/jobs/view/?currentJobId=1234567890
   ```

---

## Forking & Testing

1. Fork the repo and clone it
2. `pip install -r requirements.txt`
3. Copy `.env.example` → `.env`, add your OpenAI key
4. Replace `resume.yaml` with your own (or upload in the UI)
5. `streamlit run app.py`

The `mycustomtheme/` directory is included — RenderCV needs it to render PDFs with this style. To use a built-in theme instead, change `design.theme` in the YAML to `classic`, `sb2nov`, or another [built-in theme](https://docs.rendercv.com/user_guide/available_themes/).

---

## Requirements

- Python 3.11+
- OpenAI API key (GPT-4o access)
- `rendercv` — requires a LaTeX distribution ([TinyTeX](https://yihui.org/tinytex/) or TeX Live)
- RapidAPI key — optional, only for LinkedIn URL scraping

---

## License

MIT
