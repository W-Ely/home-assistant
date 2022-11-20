import os
import json

import requests

import hassapi as hass

HEADERS = {"Content-type": "application/json"}
URL =  "https://hooks.slack.com/services/"


class Slack(hass.Hass):
    def initialize(self):
        self.log("Slack App: initialize")
        handle = self.listen_event(self.events, event=None)

    def events(self, event_name, event, thread, *args, **kwargs):
        self.log("Slack App: events")
        data = {
            "event_name": event_name,
            "event": event
        }
        message = {"text": json.dumps(data, indent=2)}
        requests.post(URL + self.args["slack_web_hook_uuid"], json=message, headers=HEADERS) 
