import requests
import time
import webbrowser

# The URL of the website you want to monitor
url = 'https://aadl3inscription2024.dz/'
# The YouTube URL to play when the website is back up
youtube_url = 'https://www.youtube.com/watch?v=GubZho_SG8g&ab_channel=TH1HOURCLIPS'

def is_website_up(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

while True:
    if is_website_up(url):
        print("The website is back up!")
        webbrowser.open(youtube_url)
        break
    else:
        print("Website is still down. Checking again in 1 second...")
        time.sleep(1)
