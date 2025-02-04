import json
import os
from dotenv import load_dotenv
load_dotenv()
import http.client
import json
import requests
from langchain.tools import tool

class SearchTools():    
    @tool
    def search_internet(query):
        """Search the internet about a given topic and return relevant results."""
        
        # Extract the query string from the input object
        query_str = query.get("description") if isinstance(query, dict) else str(query)
        
        API_KEY = os.getenv("SERPER_API_KEY")  # Fetch API key from environment variable
        if not API_KEY:
            return "Error: API key is missing. Please set the SERPER_API_KEY environment variable."

        url = "https://google.serper.dev/search"
        headers = {
            'X-API-KEY': API_KEY,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"q": query_str})

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 403:
            return "Error: Unauthorized. Check if the API key is correct and has access to Serper.dev search."

        if response.status_code != 200:
            return f"Error: API request failed with status {response.status_code}. Response: {response.text}"

        try:
            response_data = response.json()
        except json.JSONDecodeError:
            return "Error: Invalid JSON response from API."

        if "organic" not in response_data:
            return "No search results found. Ensure your query is relevant."

        results = response_data["organic"]
        formatted_results = []

        for result in results[:4]:  # Return top 4 results
            try:
                formatted_results.append(
                    f"Title: {result['title']}\nLink: {result['link']}\nSnippet: {result['snippet']}\n-----------------"
                )
            except KeyError:
                continue  # Skip any incomplete result

        return "\n".join(formatted_results) if formatted_results else "No relevant results found."
