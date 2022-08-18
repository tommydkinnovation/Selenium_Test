from email.message import EmailMessage
import ssl
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending/'


def getDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.cookies": 2})
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_videos(driver):
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    driver.get(YOUTUBE_TRENDING_URL)
    videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")
    return videos


def send_email():

    try:
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        # server.starttls()
        # server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server_ssl.ehlo()

        email_sender = 'gkerry200@gmail.com'
        email_password = 'shtwihosbkfmshll'
        email_receiver = 'gkerry200@gmail.com'

        subject = 'Check out new ticket'
        body = """ I have just sent my first ticket!"""

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            print('Loging in...')
            smtp.login(email_sender, email_password)
            print('Sending Email...')
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        # SENDER_EMAIL = 'gkerry200@gmail.com'
        # RECEIVER_EMAIL = 'gkerry200@gmail.com'
        # subject = 'Test Message from VS CODE'
        # body = 'Hey, test message from VS Code'

        # email_text = f"""\
        # from: {SENDER_EMAIL}
        # To: {RECEIVER_EMAIL}
        # Subject: {subject}
        # {body}
        # """
    except:
        print('Something went wrong...')


def parse_video(video):
    # parse out title, url, thumbnail_url, channel, description
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')

    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_div.text

    description = video.find_element(By.ID, 'description-text').text
    return {
        'title': title,
        'url': url,
        'thumbnail': thumbnail_url,
        'channel': channel_name,
        'description': description
    }


if __name__ == "__main__":
    print('Creating Driver')
    # driver = getDriver()

    # print('Fetching the page')
    # videos = get_videos(driver)

    # # Printout number of videos found
    # print(f'Found {len(videos)} videos')

    # print('Parsing top 10 videos')
    # videos_data = [parse_video(video) for video in videos[:10]]
    # print(videos_data)
    # print('Save the data to csv')
    # videos_df = pd.DataFrame(videos_data)
    # print(videos_df)
    # videos_df.to_csv('trending.csv', index=None)
    print('Send an email with the results')
    send_email()

    # # calling the first video
    # video = videos[0]

    # print('Title: ', title)
    # print('URL: ', url)
    # print('Thumbnail URL: ', thumbnail_url)
    # print('Channel Name: ', channel_name)
    # print('Description: ', description)
