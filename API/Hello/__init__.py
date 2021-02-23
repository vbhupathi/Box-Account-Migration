# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import os
import logging
from boxsdk import Client
from boxsdk import JWTAuth


def main(name: str) -> str:
    return f"Hello {name}!"    
def createBoxClient()
    configJson = os.getenv('BoxConfigJson')
    config = JWTAuth.from_settings_file(configJson)
    return Client(config)
def getCurrentUser()
    boxClient = createBoxClient()
    current_user = boxClient.user().get()





