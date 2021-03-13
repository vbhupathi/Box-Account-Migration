# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from _init_ import itemParams
from _init_ import createBoxUserClient 

# Remove Items
def main(items: list(itemParams)) -> str:
    boxClient = createBoxUserClient(items.userId)
    for item in items
        if item.itemType == 'file':
            boxClient.file(file_id=item.id).delete()
        if item.itemType == 'folder':
            boxClient.folder(folder_id=item.id, recursive:true).delete()
        if item.type == 'collaboration':
            removeCollaboration(item.id)
    return f"Removed item {item.id}, {item.Name}, {item.type}!"

# Remove Collaboration
def removeCollaboration(collabId: str) -> str:
    boxClient.collaboration(collabId).delete()
