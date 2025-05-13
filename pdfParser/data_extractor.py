import requests
import json

def extract_resume_info(resume_text):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"
    
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": "AIzaSyARSh3HFFuwsPCf5sP_TLUBh2fougaVCUA"
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": f"""
                Extract the following information from this resume and return it as a JSON object:
                1. Name (full name of the person)
                2. Email address
                3. Phone number (in standard format)
                4. Skills (as an array of strings)
                5. Experience (as an array of work experiences with descriptions)
                6. Education (as an array of educational qualifications)
                
                Return ONLY valid JSON. The format should be:
                {{
                    "name": "John Doe",
                    "email": "john@example.com",
                    "phone": "+123456789",
                    "skills": ["Python", "JavaScript", "Machine Learning"],
                    "experience": ["Senior Developer at XYZ (2018-2021): Led development team", "Junior Developer at ABC (2015-2018): Built web applications"],
                    "education": ["MSc Computer Science, University of Technology (2015)", "BSc Computer Science, State University (2013)"]
                }}

                Here is the resume text:
                {resume_text}
                """
            }]
        }]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        try:
            response_text = result["candidates"][0]["content"]["parts"][0]["text"]
            # Process the response text to extract JSON
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0].strip()
            else:
                json_str = response_text
            
            return json.loads(json_str)
        except Exception as e:
            return {"error": f"Failed to parse response: {str(e)}"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}