import os
import requests

# Constants
TOKEN_FILE_PATH = '/sdcard/TOKENCHECKER/token/token.txt'
FACEBOOK_API_URL = 'https://graph.facebook.com/me?fields=id&access_token={token}'

def read_tokens(file_path):
    """Read tokens from the given file path."""
    with open(file_path, 'r') as file:
        tokens = [line.strip() for line in file.readlines()]
    return tokens

def check_duplicates(tokens):
    """Check for duplicate tokens in the list."""
    seen = set()
    duplicates = set()
    for token in tokens:
        if token in seen:
            duplicates.add(token)
        seen.add(token)
    return list(duplicates)

def verify_token(token):
    """Verify if the token is valid by making a request to the Facebook API."""
    response = requests.get(FACEBOOK_API_URL.format(token=token))
    return response.status_code == 200

def main():
    # Read tokens from the file
    tokens = read_tokens(TOKEN_FILE_PATH)
    
    # Count tokens
    total_tokens = len(tokens)
    
    # Check for duplicates
    duplicates = check_duplicates(tokens)
    duplicate_count = len(duplicates)
    
    # Verify tokens and count valid ones
    valid_tokens = []
    for token in tokens:
        if verify_token(token):
            valid_tokens.append(token)
    
    # Create dashboard
    print("Dashboard:")
    print(f"Total Tokens: {total_tokens}")
    print(f"Total Duplicates: {duplicate_count}")
    print(f"Valid Tokens Count: {len(valid_tokens)}")
    
    if duplicate_count > 0:
        print("\nDuplicates Found:")
        for dup in duplicates:
            print(f"- {dup}")

    print("\nValid Tokens:")
    for token in valid_tokens:
        print(f"- {token}")

if __name__ == '__main__':
    main()
