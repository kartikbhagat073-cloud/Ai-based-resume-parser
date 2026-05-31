from gpt4all import GPT4All
import pdfplumber

# Load GPT4All model
model = GPT4All(" your GP4ALL MODEL ")

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_resume_data_llm(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    
    # Prompt for LLM
    prompt = f"""
    Extract the following details from this resume:
    - Full Name
    - Email
    - Phone Number
    - Skills (as a list)
    - Work Experience (summary)
    
    Resume Text:
    {text}
    """
    
    # Generate Response
    response = model.generate(prompt)
    
    # Sample Response Format (depends on the prompt structure)
    extracted_data = {
        "name": extract_value(response, "Full Name"),
        "email": extract_value(response, "Email"),
        "phone": extract_value(response, "Phone Number"),
        "skills": extract_value(response, "Skills").split(", "),
        "experience": extract_value(response, "Work Experience")
    }

    return extracted_data

# Helper Function to Extract Values
import re
def extract_value(response, field):
    match = re.search(rf"{field}:\s*(.*)", response)
    return match.group(1).strip() if match else "Not Found"


