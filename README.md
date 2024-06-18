# YouTube Channel Video Scraper

## Overview

This script scrapes video data from a YouTube channel using Selenium WebDriver. It collects video titles, URLs, view counts, posting dates, and the top comments, then saves the data to a CSV file.

## Prerequisites

1. Python 3.x
2. Chrome browser
3. Google ChromeDriver
4. The following Python packages:
   - `selenium`
   - `webdriver_manager`
   - `pandas`

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages using pip:

    ```bash
    pip install selenium webdriver_manager pandas
    ```

## Usage

1. Open the script in your favorite text editor or IDE.
2. Set the `CHANNEL_URL` variable to the URL of the YouTube channel you want to scrape.
3. Run the script:

    ```bash
    python scraper.py
    ```

## Script Details

- The script initializes a Selenium WebDriver for Chrome.
- It navigates to the specified YouTube channel URL and clicks on the "Videos" tab.
- It scrolls through the video list to load more videos.
- For each video, it collects the title, URL, view count, posting date, and top comments.
- The data is saved to a CSV file named `youtube_videos_data.csv`.

## Functions

### `scrape_channel_videos(channel_url)`

- **Parameters**: `channel_url` (str): The URL of the YouTube channel.
- **Returns**: A pandas DataFrame containing the scraped video data.

## Example

To scrape videos from the TED YouTube channel, you can use the script as follows:

```python
CHANNEL_URL = "https://www.youtube.com/c/TED"
df_videos = scrape_channel_videos(CHANNEL_URL)
df_videos.to_csv('youtube_videos_data.csv', index=False)
```
