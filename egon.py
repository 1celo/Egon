# egon spammer yuhhh

import requests
import json
import time
import webbrowser
import os
from colorama import Fore, Style, init
from termcolor import colored
from pyfiglet import Figlet

# Initialize colorama
init(autoreset=True)

def set_window_size():
    """Set the terminal window size"""
    # Width based on the separator line (50 characters)
    width = 55  # Adding a small buffer
    height = 25  # A reasonable height that's a bit smaller
    
    if os.name == 'nt':  # For Windows
        os.system(f'mode con: cols={width} lines={height}')
    else:  # For Unix/Linux
        os.system(f'printf "\033[8;{height};{width}t"')

def set_window_title(title):
    """Set the terminal window title"""
    if os.name == 'nt':  # For Windows
        os.system(f'title {title}')
    else:  # For Unix/Linux/MacOS
        print(f'\033]0;{title}\007', end='')

def display_logo():
    """Display the Egon logo in pink"""
    f = Figlet(font='slant')
    logo_text = f.renderText("      EGON")
    
    # Print the logo in pink
    print(Fore.MAGENTA + logo_text + Style.RESET_ALL)
    print(Fore.MAGENTA + "              Discord Webhook Spammer" + Style.RESET_ALL + "\n")
    print("-" * 50)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def send_webhook_message(webhook_url, content):
    """Send a message to a Discord webhook"""
    data = {
        "content": content
    }
    
    try:
        result = requests.post(
            webhook_url,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        result.raise_for_status()
        return True, "Message sent successfully!"
    except requests.exceptions.HTTPError as err:
        return False, f"HTTP Error: {err}"
    except requests.exceptions.ConnectionError:
        return False, "Connection Error: Failed to connect to the webhook"
    except requests.exceptions.Timeout:
        return False, "Timeout Error: Request timed out"
    except requests.exceptions.RequestException as err:
        return False, f"Error: {err}"

def validate_webhook_url(url):
    """Validate if the URL is a Discord webhook URL"""
    return url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/")

def validate_delay(delay_str):
    """Validate and convert delay string to float"""
    try:
        delay = float(delay_str)
        if delay < 0:
            return False, "Delay cannot be negative"
        return True, delay
    except ValueError:
        return False, "Please enter a valid number for delay"

def main():
    """Main function to run the Egon tool"""
    # Set window size
    set_window_size()
    
    set_window_title("Egon - Discord Webhook Tool")

    # Open the URL on launch
    webbrowser.open("https://guns.lol/1celo")
    
    clear_screen()
    display_logo()
    
    # Get webhook URL
    while True:
        webhook_url = input(f"{Fore.CYAN}Enter Discord Webhook URL: {Style.RESET_ALL}")
        if validate_webhook_url(webhook_url):
            break
        print(f"{Fore.RED}Invalid webhook URL. It should start with 'https://discord.com/api/webhooks/'{Style.RESET_ALL}")
    
    # Get message
    print(f"\n{Fore.CYAN}Enter the message you want to send:{Style.RESET_ALL}")
    message = input("> ")
    
    # Get delay
    while True:
        delay_input = input(f"\n{Fore.CYAN}Enter delay between messages (in seconds): {Style.RESET_ALL}")
        valid, result = validate_delay(delay_input)
        if valid:
            delay = result
            break
        print(f"{Fore.RED}{result}{Style.RESET_ALL}")
    
    # Confirm information
    clear_screen()
    display_logo()
    
    print(f"{Fore.GREEN}Please confirm your information:{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}Webhook URL:{Style.RESET_ALL} {webhook_url}")
    print(f"{Fore.YELLOW}Message:{Style.RESET_ALL} {message}")
    print(f"{Fore.YELLOW}Delay:{Style.RESET_ALL} {delay} seconds")
    
    confirm = input(f"\n{Fore.CYAN}Is this information correct? (y/n): {Style.RESET_ALL}").lower()
    
    if confirm == 'y' or confirm == 'yes':
        print(f"\n{Fore.GREEN}Starting to send messages...{Style.RESET_ALL}")
        
        count = 0
        try:
            while True:
                success, message_result = send_webhook_message(webhook_url, message)
                count += 1
                
                if success:
                    print(f"{Fore.GREEN}[{count}] {message_result}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[{count}] {message_result}{Style.RESET_ALL}")
                    break
                
                time.sleep(delay)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Process interrupted by user. Sent {count} messages.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}Operation cancelled. Restart the program to try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Program terminated by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
    
    input("\nPress Enter to exit...")
