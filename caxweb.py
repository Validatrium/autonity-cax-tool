import os
import time
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def save_env_var(key, value):
    with open('.env', 'a') as f:
        f.write(f'{key}={value}\n')

def get_input(prompt):
    return input(prompt).strip()

def generate_api_key():
    has_apikey = get_input("Do you already have an API key? (1 for Yes, 2 for No): ")
    
    if has_apikey == "1":
        pasted_apikey = get_input("Paste your API key: ")
        save_env_var('APIKEY', pasted_apikey)
        print("Congratulations! You have successfully added your API KEY to .env.")
    elif has_apikey == "2":
        message = json.dumps({"nonce": str(int(time.time() * 1e9))})
        with open('message.sig', 'w') as sig_file:
            # Here, you need to integrate with `aut` to sign the message
            # This is just a placeholder
            signed_message = "signed_message_placeholder"
            sig_file.write(signed_message)
        
        response = requests.post(
            "https://cax.piccadilly.autonity.org/api/apikeys",
            headers={"api-sig": f"@message.sig"},
            data=message
        )
        new_api_key = response.json().get('apikey')
        save_env_var('APIKEY', new_api_key)
        print("Congratulations! You have successfully obtained an API KEY and saved it to .env.")

def main():
    actions = {
        "1": generate_api_key,
        # Add other actions here
    }
    
    while True:
        if not os.path.exists('.env'):
            print("Error: .env file not found.")
            return
        
        load_dotenv()

        print("Action options:")
        print("1. Generate API Key")
        # Add other action descriptions here
        print("10. Exit")
        
        choice = get_input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")
        
        if choice == "10":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
