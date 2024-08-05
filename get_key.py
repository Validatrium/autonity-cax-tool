import os

def get_aut_api_key():
    root_path = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(root_path, '../.data/.autonity/autonity_api.token')
    
    with open(token_path, 'r') as token_file:
        api_key = json.load(token_file).get('apikey')
        print(api_key)

if __name__ == "__main__":
    get_aut_api_key()
