# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from _init_ import createBoxUserClient 


# Purge all the trashed items
def main(args: itemParams) -> str:
    boxClient = createBoxUserClient(items.userId)
    if args.itemType == "file":
        file = boxClient.file(file_id = args.itemId)
        boxClient.trash().permanently_delete_item(file)
    print('The file was deleted from trash!')
    if args.itemType == "folder":
        folder = boxClient.folder(folder_id = args.itemId)
        boxClient.trash().permanently_delete_item(folder)
    print('The folder was deleted from trash!')
    return f"Trashed Items are deleted permanently!"
