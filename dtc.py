import requests
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

TOKEN_FILE = '/sdcard/TOKENCHECKER/token/token.txt'
LOG_FILE = '/sdcard/TOKENCHECKER/credentials/log.txt'

def create_file_if_not_exists(file_path):
    """Ensure the directory and file exist."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            pass  # Create an empty file

def check_facebook_token(token):
    """Check the validity of the Facebook token."""
    url = f'https://graph.facebook.com/me?fields=id&access_token={token}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        uid = data.get('id', '')
        if uid.startswith(('615', '100')):
            return 'valid', 'user', uid
        else:
            return 'valid', 'page', uid
    return 'invalid', None, None

def process_tokens():
    """Process tokens to determine their validity and handle duplicates."""
    # Ensure both TOKEN_FILE and LOG_FILE exist
    create_file_if_not_exists(TOKEN_FILE)
    create_file_if_not_exists(LOG_FILE)

    valid_tokens = []
    invalid_tokens = []
    duplicates = set()

    token_counts = {}
    
    user_count = 0
    page_count = 0

    with open(TOKEN_FILE, 'r') as file:
        tokens = file.read().splitlines()

    with open(LOG_FILE, 'a') as log_file:
        for token in tokens:
            # Count occurrences of each token
            if token in token_counts:
                token_counts[token] += 1
            else:
                token_counts[token] = 1

            status, token_type, uid = check_facebook_token(token)
            if status == 'valid':
                valid_tokens.append(token)
                log_message = f'{uid} : {token_type} : {status}'
                log_file.write(log_message + '\n')
                if token_type == 'user':
                    user_count += 1
                    print(f'{Fore.GREEN}{log_message}{Style.RESET_ALL}')  # Print in green for valid user
                elif token_type == 'page':
                    page_count += 1
                    print(f'{Fore.GREEN}{log_message}{Style.RESET_ALL}')  # Print in green for valid page
            else:
                invalid_tokens.append(token)
                log_message = f'Unknown ID : {status}'
                log_file.write(log_message + '\n')
                print(f'{Fore.RED}{log_message}{Style.RESET_ALL}')  # Print in red for invalid
            
            time.sleep(0)  # To prevent hitting rate limits

    # Identify duplicates
    duplicates = {token for token, count in token_counts.items() if count > 1}
    total_duplicates = sum(count - 1 for count in token_counts.values() if count > 1)

    # Save valid tokens back to the TOKEN_FILE
    with open(TOKEN_FILE, 'w') as file:
        file.write('\n'.join(valid_tokens))
    
    total_tokens = len(valid_tokens) + len(invalid_tokens)
    
    print("\n" + Fore.CYAN + "Dashboard Summary:" + Style.RESET_ALL)
    print(f"{Fore.GREEN}Total User Accounts: {Fore.YELLOW}{user_count}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Total Page Accounts: {Fore.YELLOW}{page_count}{Style.RESET_ALL}")
    print(f"{Fore.RED}Total Disabled: {Fore.YELLOW}{len(invalid_tokens)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Total Alive: {Fore.YELLOW}{len(valid_tokens)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Total Accounts: {Fore.YELLOW}{total_tokens}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Total Duplicate Tokens: {Fore.YELLOW}{total_duplicates}{Style.RESET_ALL}")

    if duplicates:
        print(f"\n{Fore.MAGENTA}Duplicates Found:{Style.RESET_ALL}")
        for token in duplicates:
            print(f"- {token}")

if __name__ == '__main__':
    process_tokens()
