# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import os
import azure.functions as func
import azure.durable_functions as df
from boxsdk import OAuth2, Client
from boxsdk import JWTAuth
from _init_ import ActivateUser, GetAllItems, RemoveItems, ListTrashedItems, PurgeTrashedItems, RollOutUserAccount

def orchestrator_function(context: df.DurableOrchestrationContext):
    args = migrationParams(context.get_input())

    yield context.call_activity('ActivateUserAccount', args.userId)
    items = yield itemParams(context.call_activity('GetAllItems', args))
    yield [contex.call_activity('RemoveItems', item) for item in items ]    
    trashedItems = yield itemParams(context.call_activity('ListAllTrashedItems', args))
    yield [context.call_activity('PurgeTrashedItems', item) for item in items]
    yield context.call_activity('RollOutUserAccount', args.userId)

main = df.Orchestrator.create(orchestrator_function)

def createBoxClient():
    configJson = os.getenv('BoxConfigJson')
    auth = JWTAuth.from_settings_file(configJson)
    return Client(auth)
def createBoxUserClient(userId):
    user = client.user(user_id=userId)
    configJson = os.getenv('BoxConfigJson')
    auth = JWTAuth.from_settings_file(configJson)
    auth.authenticate_user()
    user_client = Client(auth)

def getCurrentUser():
    boxClient = createBoxClient()
    current_user = boxClient.user().get()
