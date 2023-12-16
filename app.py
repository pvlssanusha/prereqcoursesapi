from flask import Flask, request, jsonify
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Replace 'YOUR_COHERE_API_KEY' with your Cohere API key

# Initialize the Cohere Client with an API Key
api = os.getenv("GEMINI_API_KEY")
api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['POST'])
def get_response():
    try:
        coursename = request.get_json().get('coursename')
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": 
                            f'''
        From the given course {coursename} give the prerequiste courses required to learn that course 
            Can you create a table of prerequiste courses for it?
            Give the output in json format as code block:
            {{
                
                "prereqcourses": ["strings"],
                
            }}
            
        '''
                        }
                    ]
                }
            ]
        }

        # Set the headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the API call
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Parse and print the response JSON
            response_json = response.json()
            #print(response_json["candidates"][0]["content"]["parts"][0]["text"][7:-3])
            return (response_json["candidates"][0]["content"]["parts"][0]["text"][7:-3])
            # print(json.dumps(response_json, indent=2))
            # print(response_json)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return json.dump(
            {
                "msg":"Error Assessing AI"
            }
            ) 

    except Exception as e:
        return jsonify({'error': str(e)})


# ... (your existing code)

@app.route('/module', methods=['POST'])
def get_course_content():
    try:
        modulename = request.get_json().get('modulename')
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f'''
                                I want {modulename} content in 200 words covering almost all the contents in the {modulename}.
                                Can you create a table of contents for it?
                                Give the output in json format as code block:
                                {{
                                    "content": "string"
                                }}
                            '''
                        }
                    ]
                }
            ]
        }

        # Set the headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the API call
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Parse and print the response JSON
            response_json = response.json()
            content = response_json["candidates"][0]["content"]["parts"][0]["text"][7:-3]
            return jsonify({"content": content})
        
        
            
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return json.dumps({"msg": "Error assessing AI"})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/easylevel', methods=['POST'])
def get_easylevel_content():
    try:
        topic = request.get_json().get('submodulename')
        description=request.get_json().get('description')
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f'''
                                "This is the topic {topic} and also its content{description}.Please regenerate the  content in such  a way that they could understand in simple language.Keep the response fitting with atleast 400 words"
                                Give the output in json format as code block:
                                {{
                                    "easylevel":"string"
                                }}
                            '''
                        }
                    ]
                }
            ]
        }

        # Set the headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the API call
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Parse and print the response JSON
            response_json = response.json()
            content = response_json["candidates"][0]["content"]["parts"][0]["text"][7:-3]
            return jsonify({"content": content})
        
        
            
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return json.dumps({"msg": "Error assessing AI"})

    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/mediumlevel', methods=['POST'])
def get_mediumlevel_content():
    try:
        topic = request.get_json().get('submodulename')
        description=request.get_json().get('description')
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f'''
                                "This is the  topic {topic} and also its content {description},regenerate the content covering key concepts and principles."
"Describe content with moderate complexity, suitable for a high school student.Keep the response fitting with atleast 400 words"
                                Give the output in json format as code block:
                                {{
                                    "medium":"string"
                                }}
                            '''
                        }
                    ]
                }
            ]
        }

        # Set the headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the API call
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Parse and print the response JSON
            response_json = response.json()
            content = response_json["candidates"][0]["content"]["parts"][0]["text"][7:-3]
            return jsonify({"content": content})
        
        
            
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return json.dumps({"msg": "Error assessing AI"})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/hardlevel', methods=['POST'])
def get_hardlevel_content():
    try:
        topic = request.get_json().get('submodulename')
        description=request.get_json().get('description')
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f'''
                                "This is the topic {topic} and its content {description}, regenerate the content by covering intricate details, applications. Keep the response concise but comprehensive, fitting with atleasst 400 words"
                                Give the output in json format as code block:
                                {{
                                    "hardlevel":"string"
                                }}
                            '''
                        }
                    ]
                }
            ]
        }

        # Set the headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the API call
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Parse and print the response JSON
            response_json = response.json()
            content = response_json["candidates"][0]["content"]["parts"][0]["text"][7:-3]
            return jsonify({"content": content})
        
        
            
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return json.dumps({"msg": "Error assessing AI"})

    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)