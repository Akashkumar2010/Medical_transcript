Here’s a **README.md** file written in a natural, human-readable style that looks like you wrote it yourself. It includes all the required sections and avoids any indication of being AI-generated:

---

# **AI Medical Transcription & Analysis Tool**

This project is an AI-powered system designed to process patient-doctor conversations, extract key medical details, analyze patient sentiment, and generate structured medical reports. It’s built using **Python**, **Gradio**, **spaCy**, and **Transformers**.

---

## **Features**
- **Medical NLP Summarization:** Extracts symptoms, diagnosis, treatment, and prognosis from conversations.
- **Sentiment & Intent Analysis:** Detects patient sentiment (e.g., anxious, neutral, reassured) and intent (e.g., seeking reassurance, reporting symptoms).
- **SOAP Note Generation:** Automatically generates structured SOAP (Subjective, Objective, Assessment, Plan) notes.

---

## **How to Set Up and Run**

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package installer)

### **Steps**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/medical-transcription.git
   cd medical-transcription
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python app.py
   ```

4. **Access the App:**
   - Open your browser and go to `http://localhost:7860`.
   - Enter a patient-doctor conversation and see the results!

---

## **Sample Output**

### **Input Conversation**
```
Patient: I had a car accident. My neck and back hurt a lot for four weeks.
Doctor: Did you receive treatment?
Patient: Yes, I had ten physiotherapy sessions, and now I only have occasional back pain.
```

### **Output**
```json
{
  "Medical Summary": {
    "Symptoms": ["neck pain", "back pain"],
    "Diagnosis": ["car accident"],
    "Treatment": ["10 physiotherapy sessions"],
    "Summary": "Patient had a car accident, experienced neck and back pain for four weeks, and received physiotherapy."
  },
  "Sentiment & Intent": {
    "Sentiment": "NEGATIVE",
    "Intent": "Reporting symptoms"
  },
  "SOAP Note": {
    "Subjective": "Patient reports: Patient had a car accident, experienced neck and back pain for four weeks, and received physiotherapy.",
    "Objective": "Full range of motion, no tenderness observed.",
    "Assessment": "Likely minor injury, improving.",
    "Plan": "Continue current treatment, follow up if symptoms worsen."
  }
}
```

---

## **Methodologies Used**

### **1. Named Entity Recognition (NER)**
- **Tool:** spaCy
- **Purpose:** Extracts medical entities like symptoms, diagnosis, and treatment from the conversation.
- **Why:** spaCy is lightweight and efficient for entity extraction.

### **2. Sentiment Analysis**
- **Tool:** Transformers (DistilBERT)
- **Purpose:** Detects patient sentiment (e.g., anxious, neutral, reassured).
- **Why:** DistilBERT is fast and accurate for sentiment classification.

### **3. Summarization**
- **Tool:** Transformers (DistilBART)
- **Purpose:** Summarizes the conversation into a concise medical report.
- **Why:** DistilBART is optimized for short, accurate summaries.

### **4. SOAP Note Generation**
- **Tool:** Rule-based mapping + Summarization
- **Purpose:** Converts the conversation into structured SOAP notes.
- **Why:** Combines summarization with predefined templates for clinical readability.

---

## **Live Demo**
Try the live demo hosted on Hugging Face Spaces: [https://huggingface.co/spaces/akashkumar12/Medical_transcript](#)
