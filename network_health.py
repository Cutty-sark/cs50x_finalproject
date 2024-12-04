# Module for network health information
from nn import Block
from datetime import datetime
import psutil
import speedtest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime, timedelta

#outages
def scrape_outages():
    """
    Scrape outage data from Outage.Report for the last 24 hours.
    """
    url = "https://outage.report/"
    options = Options()
    options.add_argument("--headless")  # Enable headless mode for silent browsing
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("C:\webdrivers\chromedriver.exe")  # Replace with the actual path to your WebDriver

    outages = []
    try:
        # Launch the browser in headless mode
        with webdriver.Chrome(service=service, options=options) as driver:
            driver.get(url)

            # Wait for elements to load (implicit wait)
            driver.implicitly_wait(10)

            # Get services, dates, and descriptions
            services = driver.find_elements(By.CLASS_NAME, "_heading_pbnkx_21")
            dates = driver.find_elements(By.CLASS_NAME, "_date_109mf_5")
            descriptions = driver.find_elements(By.CLASS_NAME, "text-sm.text-slate-600")

            # Current date for filtering
            current_date = datetime.now().date()

            # Extract up to 3 outages from the last 24 hours
            for service, date, description in zip(services, dates, descriptions):
                try:
                    # Parse the date and filter by the last 24 hours
                    outage_date = datetime.strptime(date.text.strip(), "%Y-%m-%d").date()
                    if current_date - outage_date <= timedelta(days=1):
                        outages.append(f"{service.text}: {description.text}")
                except ValueError:
                    continue  # Skip any improperly formatted dates

                if len(outages) >= 3:
                    break

        return outages if outages else ["No major outages found in the last 24 hours."]
    except (NoSuchElementException, TimeoutException) as e:
        return [f"Error scraping outages: {e}"]
    

#speedtest
def get_network_speed():
    """Measure the current network speed using Speedtest.net."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()  # Select the best server
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        return f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps"
    except Exception as e:
        return f"Error measuring network speed: {e}"



#uptime endpoint in hrs mins secs
def get_uptime():
    connections = psutil.net_if_stats()
    active_since = None
    for interface, stats in connections.items():
        if stats.isup:
            boot_time = psutil.boot_time()
            active_since = boot_time if not active_since else min(active_since, boot_time)
    if active_since:
        connected_since = datetime.fromtimestamp(active_since)
        elapsed = datetime.now() - connected_since
        hours, remainder = divmod(elapsed.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    else:
        return "Not connected"
    



#info to be pushed to the block
class NetworkHealth(Block):
    def __init__(self):
        # Initialize the parent class with the title "Network Health"
        super().__init__("Network Health")

    def gather_data(self):

        uptime = get_uptime()
        speed = get_network_speed()
        #healthvector = [uptime, locspeed, broadout, hostout]
        # Add data specific to network health
        self.add_content(f"Current uptime: {uptime}")
        self.add_content(f"Current network speed: {speed}")
        # Scrape outages
        outages = scrape_outages()
        self.add_content("Top host outages (last 24 hrs):\n")
        for outage in outages:
            self.add_content("-" + outage + "\n")

