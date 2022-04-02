"""apprise notification"""

import os

import apprise
from dotenv import load_dotenv

# ENVPATH = os.path.join(os.path.dirname(__file__), ".env")
ENVPATH = os.path.abspath(os.curdir)
if os.path.isfile(ENVPATH):
    load_dotenv(ENVPATH)


def apprise_init():
    if "APPRISE_URL" not in os.environ:
        raise ValueError("APPRISE_URL must be set to use apprise service")

    apprise_url = os.environ.get("APPRISE_URL")
    # Point our configuration to this API server:
    config = apprise.AppriseConfig()
    config.add(apprise_url)

    # Create our Apprise Instance
    app = apprise.Apprise()

    # Store our new configuration
    app.add(config)

    return app


notify = apprise_init()
