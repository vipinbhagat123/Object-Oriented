import os
import webbrowser
import smtplib
import requests
from geopy.geocoders import Nominatim
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

def open_notepad():
    # Works on Windows to open Notepad
    os.system("notepad.exe")

def open_chrome():
    # Opens Chrome with a specific URL
    webbrowser.open("http://www.google.com")

def open_whatsapp():
    # Opens WhatsApp web
    webbrowser.open("https://web.whatsapp.com/")

def send_email():
    # Request user to input email details manually
    sender_email = input("Enter your email: ")
    password = input("Enter your email password: ")
    receiver_email = input("Enter receiver's email: ")
    subject = input("Enter subject: ")
    message_body = input("Enter your message: ")

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        # Sending email through Gmail’s SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

def send_sms():
    # Ask the user to input Twilio credentials and message details
    account_sid = input("Enter your Twilio Account SID: ")
    auth_token = input("Enter your Twilio Auth Token: ")
    from_phone = input("Enter your Twilio phone number: ")
    to_phone = input("Enter the recipient's phone number: ")
    message_body = input("Enter your message: ")

    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
    data = {
        'From': from_phone,
        'To': to_phone,
        'Body': message_body
    }

    try:
        # Sending SMS using Twilio API
        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        if response.status_code == 201:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def get_api_key():
    # Function to get API key securely
    return 'your api key'  # Replace with your actual API key

def get_chatgpt_response(messages):
    # Function to interact with the OpenAI API and get the ChatGPT response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

def chat_with_gpt():
    openai.api_key = get_api_key()

    # Initial system message to set up the assistant's behavior
    conversation = [
        {"role": "system", "content": "You are a friendly and knowledgeable assistant."}
    ]

    print("ChatGPT: Hello! How can I assist you today? (type 'exit' to stop)")

    while True:
        # Get input from the user
        user_input = input("You: ")

        # Allow user to exit the chat by typing 'exit'
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye! Have a great day.")
            break

        # Add user's message to the conversation history
        conversation.append({"role": "user", "content": user_input})

        # Get the assistant's response
        response = get_chatgpt_response(conversation)

        if response:
            # Display ChatGPT's response and add it to the conversation history
            print(f"ChatGPT: {response}")
            conversation.append({"role": "assistant", "content": response})
        else:
            print("ChatGPT: Oops, something went wrong. Please try again.")

def get_geolocation():
    # User inputs the location to geocode
    location_name = input("Enter the location to geocode: ")

    # Create a geolocator instance
    geolocator = Nominatim(user_agent="my_geolocation_app_v1.0")

    # Get location using the geocode method
    location = geolocator.geocode(location_name)

    if location:
        print(f"Location: {location.address}")
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        print("Location not found")

def get_trending_topics():
    # Ask user for Twitter API bearer token
    bearer_token = input("Enter your Twitter Bearer Token: ")

    # Get worldwide trending topics (WOEID = 1)
    url = "https://api.twitter.com/1.1/trends/place.json?id=1"

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            trends = response.json()[0]['trends']
            print("Trending topics:")
            for trend in trends:
                print(trend['name'])
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Open Notepad")
        print("2. Open Chrome")
        print("3. Open WhatsApp")
        print("4. Send Email")
        print("5. Send SMS")
        print("6. Chat with ChatGPT")
        print("7. Get Geolocation")
        print("8. Get Trending Topics on Twitter")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            open_notepad()
        elif choice == '2':
            open_chrome()
        elif choice == '3':
            open_whatsapp()
        elif choice == '4':
            send_email()
        elif choice == '5':
            send_sms()
        elif choice == '6':
            chat_with_gpt()
        elif choice == '7':
            get_geolocation() 
        elif choice == '8':
            get_trending_topics()
        elif choice == '9':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()