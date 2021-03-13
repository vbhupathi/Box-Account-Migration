# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from _init_ import itemParams
from _init_ import createBoxClient as boxAdminClient

# Activivate the user account
def ActivateUserAccount(args: itemParams) -> str:
        user = boxAdminClient.user(args.userId)
        updated_user = user.update_info({'status': 'Active'})
        return "User Account Activated!"


    