# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
 
import logging
import json

import azure.functions as func
import azure.durable_functions as df
from _init_ import orchestrator_function

class requestParams:
    def __init__(self, userEmail):
        self.userEmail = userEmail 
    @property
    def userEmail(self):
        """
        user email.
        """
        return self._userEmail
class migrationParams(requestParams):
    def __init__(self, userId):
        super().__init__(userEmail)
    @property
    def userId(self):
        """
        user id.
        """
        return self.__userId

class itemParams(migrationParams):
     # init method or constructor 
    def __init__(self, itemId, itemType, itemName): 
                super().__init__(userId, userEmail)
                self.itemId = itemId
                self.itemType = itemType
                self.itemName = itemName 
    @property
    def itemId(self):
        """
        item id.
        """
        return self.__itemId
    @property
    def itemType(self):
        """
        item type.
        """
        return self.__itemType
    @property
    def itemName(self):
        """
        item name.
        """
        return self.__itemName


async def main(req: func.HttpRequest, starter: str) -> func.HttpRequest:
    client = df.DurableOrchestrationClient(starter)
    args = requestparams(json.load())
    result = await userAccountId(args.userEmail)
    if result.success:
        margs = migrationParams(result.msg, args.userEmail)
        instance_id = await client.start_new(req.route_params["orchestrator_function"], margs)
        logging.info(f"Started orchestration with ID = '{instance_id}'.")
        return client.create_check_status_response(req, instance_id)
   # else
    #    return "User Not Found"

def singleOrDefault(sequence, default=None):
     singleItem = default
     for s in sequence:
        singleItem = s
     return singleItem

def single(sequence):
    for s in sequence:
        return s

async def userAccountId(userEmail: str) -> str:
    boxClient = createBoxClient()
    username = userEmail.Split('@')
    username = next(f for f in username)
    users = boxClient.users(filter_term=username)
    exactMatch = users.singleOrDefault(u for u in users)
    exactMatch = exactMatch.login.lower() == userEmail.lower()
    if exactMatch != null:
        print("Found Box account {0} exactly matching login.", exactMatch.id)
        return (true, exactMatch.id)
    elif users.count() > 1:
        logins = string.join(", ", list(map(lambda x: x.login, users)))
        print("Multiple Box accounts found for login: {logins}")
        return(false, "Multiple Box accounts found for login: {logins}")
    elif users.count() == 0:
        print("No Box account found for login.")
        return(false, "No Box account found for login.")
    else:
        user = users.single(u for u in users)
        return (true, user.id)