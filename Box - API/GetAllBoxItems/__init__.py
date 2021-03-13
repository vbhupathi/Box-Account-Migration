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




def GetAllBoxItems(args: itemParams) -> itemParams:
    boxClient = createBoxUserClient(args.userId)
    items = boxClient.folder(folder_id='0').get_items(fields:{"id", "name", "owned_by", "is_externally_owned", "path_collection" }, autoPaginate: true})
    ownedItems = list(for i in item if i.owned_by.id == args.userId)   

    internallyCollabedItems = for item in items if item.owned_by.id != args.userId & i.IsExternallyOwned:
                                if item.itemType == "file":
                                    getFileCollaborations(item.itemId)
                                if item.itemType == "folder":
                                    getFolderCollaborations(item.itemId)
                                print('{0} {1} is named "{2}"'.format(item.type.capitalize(), item.id, item.name))

    return ownedItems.apend(internallyCollabedItems)

# Get Folder the Collaborations
def getFolderCollaborations(itemId: str) -> str:
    collaborations = boxClient.folder(folder_id= itemId).get_collaborations(autoPaginate: true)
for collab in collaborations:
    target = collab.accessible_by & collab.ownedby 
    print('{0} {1} is collaborated on the folder'.format(target.type.capitalize(), target.name))

# Get File the Collaborations
def getFileCollaborations(itemId: str) -> str:
    collaborations = client.file(file_id=itemId).get_collaborations()
    for collab in collaborations
        target = collab.accessible_by & collab.ownedby
        print('{0} {1} is collaborated on the file'.format(target.type.capitalize(), target.name))
