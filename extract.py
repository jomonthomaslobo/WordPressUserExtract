# Extract WordPress Usernames
# Author: @jomonthomaslobo

import sys
import requests

def print_banner():
    print("WordPress User Extractor")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("Author: @jomonthomaslobo")
    print("------------------------------------------------------------------------------------------------")
    print("This application is for educational purposes only. The developer is not responsible for any misuse.")
    print("------------------------------------------------------------------------------------------------")

def validate_arguments():
    if len(sys.argv) == 1:
        print("Arguments are missing. Usage: python3 extract.py --url <url>")
        sys.exit(1) 
    if len(sys.argv) > 3:
        print("Too many arguments. Usage: python3 extract.py --url <url>")
        sys.exit(1)
    if sys.argv[1] != "--url" or not sys.argv[2]:
        print("Arguments are missing. Usage: python3 extract.py --url <url>")
        sys.exit(1)

def extract_users(base_url):
    print(f"Connecting to {base_url}")
    
    api_url = f"{base_url}/wp-json/wp/v2/users"
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        users = response.json()
        if users:
            for user in users:
                print(f"Found User ID: {user['id']} : Username: {user['name']}")
        else:
            print("No users found.")

    except requests.exceptions.RequestException as e:
        print(f"Unable to connect to the site: {e}")
        sys.exit(1)

    print("------------------------------------------------------------------------------------------------")
    print("Extraction completed")
    print("------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    print_banner()
    validate_arguments()

    base_url = sys.argv[2]
    extract_users(base_url)

    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
