import os

remote_driver = os.getenv("REMOTE_DRIVER", "False") == "True"

SELENOID_URL = os.getenv("SELENOID_URI", "http://selenoid:4444/wd/hub")
BROWSER_NAME = os.getenv("BROWSER", "chrome")
BROWSER_VERSION = os.getenv("BROWSER_VERSION", "128.0")