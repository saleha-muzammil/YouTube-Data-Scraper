from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

def scrape_channel_videos(channel_url):
    driver.maximize_window()
    driver.get(channel_url)
    time.sleep(5)

    videos_tab = driver.find_element(By.XPATH, """//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]""")
    videos_tab.click()
    time.sleep(5)

    video_data = []

    for j in range(0):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-rich-item-renderer")))
        except TimeoutException:
            break 

    videos = driver.find_elements(By.CSS_SELECTOR, "ytd-rich-item-renderer")
    for video in videos:
        try:
            link_element = video.find_element(By.CSS_SELECTOR, "a#video-title-link")
            title = link_element.text
            video_url = link_element.get_attribute('href')
            video_data.append((title, video_url))
        except Exception as e:
            print(f"Error processing video element: {e}")
            continue

    data = []
    for title, url in video_data:
        driver.get(url)
        time.sleep(5)  

        driver.execute_script("window.scrollBy(0,500);")


        expand_metadata_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-watch-metadata")))
        expand_metadata_button.click()

        views_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'yt-formatted-string') and contains(text(), 'views')]"))) 
        views = views_element.text

        date_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='style-scope yt-formatted-string bold' and contains(text(), ', 20')]")))
        posted_date = date_element.get_attribute('aria-label')

        for j in range(2):
            driver.execute_script("window.scrollBy(0,1000);")
            time.sleep(2)

        comments = []
        comment_elements = driver.find_elements(By.XPATH, """//*[@id="content-text"]/span""")
        for comment in comment_elements:
            comments.append(comment.text)

        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Views: {views}")
        print(f"Posted Date: {posted_date}")
        print(f"Comments: {comments[:10]}")

        data.append({
            'Title': title,
            'Video URL': url,
            'Views': views,
            'Posted Date': posted_date,
            'Comments': comments[:10]  
        })

    return pd.DataFrame(data)

# Define the YouTube channel URL
CHANNEL_URL = "https://www.youtube.com/c/TED"

# Use the function
df_videos = scrape_channel_videos(CHANNEL_URL)
df_videos.to_csv('youtube_videos_data.csv', index=False)

# Close the driver
driver.quit()
