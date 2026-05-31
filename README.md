# 📄 Resume Data Extractor using LLM

A Python tool that extracts structured information from PDF resumes using a local LLM (Llama 3.2 via GPT4All) and PDF text parsing via `pdfplumber`.

---

## 🚀 Features

- Extracts key resume fields automatically:
  - Full Name
  - Email Address
  - Phone Number
  - Skills (as a list)
  - Work Experience (summary)
- Runs **fully offline** using a local GGUF model via GPT4All
- Parses PDF resumes using `pdfplumber`
- No API keys or internet connection required

---

## 🧰 Tech Stack

| Component     | Library / Tool                        |
|---------------|---------------------------------------|
| LLM Inference | [GPT4All](https://github.com/nomic-ai/gpt4all) |
| PDF Parsing   | [pdfplumber](https://github.com/jsvine/pdfplumber) |
| Language      | Python 3.8+                           |
| Model Used    | `Llama-3.2-3B-Instruct-Q4_0.gguf`    |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-extractor.git
cd resume-extractor
```

### 2. Install dependencies

```bash
pip install gpt4all pdfplumber
```

### 3. Download the LLM model

Download the `Llama-3.2-3B-Instruct-Q4_0.gguf` model from the [GPT4All model library](https://gpt4all.io/models/gguf/Llama-3.2-3B-Instruct-Q4_0.gguf) and place it at your desired path.

Update the model path in the script:

```python
model = GPT4All("C:/Users/YourName/path/to/Llama-3.2-3B-Instruct-Q4_0.gguf")
```

---

## 🗂️ Project Structure

```
resume-extractor/
│
├── resume_extractor.py   # Main script
├── README.md             # Project documentation
└── sample_resume.pdf     # (Optional) Test resume
```

---

## 🔧 Usage

```python
from resume_extractor import extract_resume_data_llm

result = extract_resume_data_llm("path/to/your/resume.pdf")
print(result)
```

### Example Output

```python
{
    "name": "Jane Doe",
    "email": "jane.doe@email.com",
    "phone": "+1-234-567-8900",
    "skills": ["Python", "Machine Learning", "SQL", "TensorFlow"],
    "experience": "5 years as a Data Scientist at XYZ Corp, focused on NLP and predictive modeling."
}
```

---

## ⚙️ How It Works

1. **PDF Text Extraction** — `pdfplumber` reads and extracts raw text from every page of the PDF resume.
2. **Prompt Construction** — The extracted text is embedded into a structured prompt asking the LLM to identify specific resume fields.
3. **LLM Inference** — GPT4All runs the Llama model locally to generate a response based on the prompt.
4. **Field Parsing** — A regex helper (`extract_value`) scans the LLM response and pulls out each labelled field.

---

## ⚠️ Limitations

- Extraction accuracy depends on the quality and format of the resume PDF.
- The regex-based parser expects the LLM to follow a strict `Field: Value` output format — inconsistent LLM responses may lead to `"Not Found"` values.
- Very long resumes may exceed the model's context window.
- Scanned (image-based) PDFs are not supported — `pdfplumber` requires text-layer PDFs.

---

## 🛠️ Potential Improvements

- Add support for scanned PDFs using OCR (e.g., `pytesseract`)
- Export extracted data to JSON or CSV
- Build a simple web UI using Streamlit or Flask
- Improve parsing with structured output prompting or JSON mode

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [GPT4All by Nomic AI](https://github.com/nomic-ai/gpt4all)
- [pdfplumber by Jeremy Singer-Vine](https://github.com/jsvine/pdfplumber)
- Meta's [Llama 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/) model
