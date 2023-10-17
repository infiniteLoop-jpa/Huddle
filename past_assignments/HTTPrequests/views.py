from django.shortcuts import render

# Create your views here - Julia
import requests
from django.http import HttpResponse

def fetch_and_print_web_page(request):
    try:
        url_to_fetch = "https://www.example.com"  # Replace with the URL you want to fetch
        # Make a GET request to the specified URL
        response = requests.get(url_to_fetch)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the content of the response (the HTML of the website)
            web_page_content = response.text
            return HttpResponse(f"Web Page Content:<br>{web_page_content}")
        else:
            return HttpResponse(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

