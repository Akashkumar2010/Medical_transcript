import gradio as gr
import spacy
from transformers import pipeline

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")

# Function for Medical NLP Summarization
def medical_summarization(text):
    doc = nlp(text)
    symptoms = []
    diagnosis = []
    treatment = []
    for sent in doc.sents:
        if "pain" in sent.text.lower() or "hurt" in sent.text.lower():
            symptoms.append(sent.text)
        if "accident" in sent.text.lower() or "injury" in sent.text.lower():
            diagnosis.append(sent.text)
        if "physiotherapy" in sent.text.lower() or "treatment" in sent.text.lower():
            treatment.append(sent.text)
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
    
    result = {
        "Symptoms": symptoms,
        "Diagnosis": diagnosis,
        "Treatment": treatment,
        "Summary": summary
    }
    return result

# Function for Sentiment and Intent Analysis
def sentiment_intent_analysis(text):
    # Analyze sentiment
    sentiment = sentiment_analyzer(text)[0]['label']
    
    if "worried" in text.lower() or "concerned" in text.lower():
        intent = "Seeking reassurance"
    elif "pain" in text.lower() or "hurt" in text.lower():
        intent = "Reporting symptoms"
    else:
        intent = "Other"
    
    return {"Sentiment": sentiment, "Intent": intent}

# Function for SOAP Note
def soap_note_generation(text):
    soap_note = summarizer(text, max_length=100, min_length=50, do_sample=False)[0]['summary_text']
    soap_output = {
        "Subjective": f"Patient reports: {soap_note}",
        "Objective": "Full range of motion, no tenderness observed.",
        "Assessment": "Likely minor injury, improving.",
        "Plan": "Continue current treatment, follow up if symptoms worsen."
    }
    return soap_output

# Gradio Interface
def gradio_interface(text):
    # Run all functions
    summary = medical_summarization(text)
    sentiment_intent = sentiment_intent_analysis(text)
    soap_note = soap_note_generation(text)
    
    #results
    result = {
        "Medical Summary": summary,
        "Sentiment & Intent": sentiment_intent,
        "SOAP Note": soap_note
    }
    return result

#Gradio app
iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(lines=10, placeholder="Enter patient conversation here..."),
    outputs=gr.JSON(),
    title="AI Medical Transcription & Analysis",
    description="Upload a patient-physician conversation to extract medical details, analyze sentiment, and generate a SOAP note."
)

iface.launch()