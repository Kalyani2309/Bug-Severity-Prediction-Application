# import requests

# base_url = "http://pratiklondhe4.pythonanywhere.com"


# def get_severity(desc):
#     req = base_url+"/predict"
#     data = {
#         "bug_description": desc,
#         "model_choice": "nb"}
#     r = requests.post(url=req, json=data)
#     print(r)
#     # Remove quotes from the response text
#     return r.text.strip('"').rstrip('"')[0:-2]


import requests

base_url = "http://pratiklondhe4.pythonanywhere.com"

def get_severity(desc):
    # Define the request URL
    url = base_url + "/predict"

    # Prepare the request data
    data = {
        "bug_description": desc,
        "model_choice": "nb"
    }

    try:
        # Send a POST request to the URL with JSON data
        response = requests.post(url, json=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the prediction result from the response text
            result = response.text.strip('"').rstrip('"')[0:-2]
            return result
        else:
            # Handle the case where the request was not successful
            print(f"Request to {url} failed with status code {response.status_code}")
    except requests.RequestException as e:
        # Handle exceptions that may occur during the request
        print(f"Request to {url} failed with an exception: {e}")
    
    # Return a default value or handle the error as needed
    return "Unknown"  # You can choose an appropriate default value or raise an exception here
