# Module for network health information
from nn import Block
from datetime import datetime
import psutil
import speedtest

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
        self.add_content("Major broadband outages (last 24 hrs): Comcast, AT&T")
        self.add_content("Top host outages (last 24 hrs): Cloudflare, Google")

