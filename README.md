# AI-Powered Phishing & Social Engineering Detector 🛡️🤖

A defensive cybersecurity tool designed to combat modern social engineering threats. This project leverages Large Language Models (LLMs) via the Google Gemini API to automatically analyze suspicious emails, text messages, and URLs, acting as an automated First-Line Response Analyst.

---

## 💡 Why This Project Matters
In modern corporate environments, Social Engineering and Phishing remain the #1 entry point for devastating cyberattacks (such as Ransomware and Data Breaches). 

This tool serves as an Automated Triage System, helping non-technical employees verify suspicious messages instantly, thereby reducing human error and lifting the burden off enterprise Security Operations Center (SOC) teams.

---

## 🌟 Key Features
* Advanced Social Engineering Triaging: Uses NLP to dissect high-pressure language, urgency triggers, and psychological manipulation.
* Comprehensive Security Report: Generates a structured output providing a clear Verdict (PHISHING/SAFE), a Confidence Score, detailed Red Flags, and actionable Recommendations.
* Production-Ready Core Logic: Built with clean, exception-handled Python code, optimized for seamless integration into email clients (like Outlook/Gmail) or web webhooks.

---

## 🛠️ Built With
* Python 3: Core Backend Logic
* Google GenAI SDK: Advanced Threat Intelligence Layer via gemini-2.5-flash

---

## 🚀 How to Run & Test

# 1. Clone the repository
To copy this project to your local machine, run the following command in your terminal:

```bash
git clone [https://github.com/Alry1/AI-Phishing-Detector.git](https://github.com/Alry1/AI-Phishing-Detector.git)
cd AI-Phishing-Detector

 2. Install Dependencies
Install the required Google GenAI library using pip:


pip install -r requirements.txt

 3. Set Up Your API Key
Open the ⁠detector.py⁠ file and insert your personal Google AI Studio secret key inside the API_KEY variable:

Python
API_KEY = "YOUR_SECURE_API_KEY"

 4. Run the Tool
Execute the Python script to start analyzing the sample phishing text:

python detector.py

🔮 Future Roadmap
 Build a web interface using Streamlit for interactive enterprise use.
 Integrate VirusTotal API for automated URL and domain reputation checks.
 Implement multi-language support to detect regional dialect phishing (e.g., local Arabic phishing campaigns).


📄 License
This project is open-source and available under the MIT License.

