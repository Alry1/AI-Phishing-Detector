from google import genai

#Put here your API key
API_KEY = "Enter-here-yor-API-key"

print("==============================================")
print("🔒 AI-Powered Phishing Detector is running... 🔒")
print("==============================================\n")


sample_email = """
URGENT: Your Netflix account will be suspended in 12 hours due to a billing issue. 
Please update your payment information immediately by clicking this link: http://netflix-billing-support-update.top/login 
Failure to update will lead to permanent account deletion.
"""

print("Sending text to Gemini AI for Cybersecurity analysis... Please wait...\n")

try:
    #Connect to Google Gemini
    client = genai.Client(api_key=API_KEY)

    prompt = f"""
    You are an expert Cybersecurity Analyst. Analyze this text for PHISHING red flags.
    Provide a clear verdict (PHISHING or SAFE), confidence score, and list the red flags.

    Text: {sample_email}
    """

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )

    print("--- 🛡️ ANALYSIS REPORT FROM AI 🛡️ ---")
    print(response.text)
    print("---------------------------------------")

except Exception as e:
    print(f"An error occurred: {e}")

print("\n[Project Execution Completed]")