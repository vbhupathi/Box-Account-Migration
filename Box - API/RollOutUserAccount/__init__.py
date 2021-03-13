# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from _init_ import createBoxClient as boxAdminClient

# Roll the user out from the enterprise
def main(args: itemParams) -> str:
    user = boxAdminClient.user(args.userId)
    updated_user = user.update_info({'enterprise': 'null'})
    return "User rolled out from the enterprise!"
