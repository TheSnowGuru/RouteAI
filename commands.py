import sys
import requests

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return {"status": "fetched", "url": url, "content": response.text}
    else:
        return {"status": "error", "url": url, "content": None}

def main():
    while True:
        # Print the command prompt in green
        print("\033[92mrouteai\033[0m")
        
        # Prompt the user to enter a URL
        url = input("Please enter a URL: ")
        
        # Fetch the URL
        fetch_result = fetch_url(url)
        print(f"Documentation been read from {url}")
        
        # Prompt the user for the next action
        action = input("Where do you want to post your call or save the data received? ")
        
        if action == "query":
            # Handle the query command
            api_key = input("Please enter your API key: ")
            endpoint = input("Please enter the endpoint: ")
            payload = input("Please enter the payload (in JSON format): ")
            
            # Send a request to the fetched API
            response = requests.post(endpoint, headers={"Authorization": f"Bearer {api_key}"}, json=payload)
            print(f"Response: {response.json()}")
        elif action == "save":
            # Save the data received
            key = input("Please enter the key to save the data: ")
            save_payload(key, fetch_result["content"])
            print(f"Data saved with key: {key}")
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
