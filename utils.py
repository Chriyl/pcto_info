from flask import request

def getReqParams(*id: str) -> dict[str: str]:
    retVal = {}
    for param in id: 
        retVal[param] = request.form.get(param, "")
    
    return retVal

def isEmpty(items: list) -> bool:
    if all(items):
        return True

    return False