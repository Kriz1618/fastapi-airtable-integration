

def serializeDict(a) -> dict:
    if a:
        return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}
    return "No changes"


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
