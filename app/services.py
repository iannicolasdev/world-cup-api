from app.data.world_cups import world_cups

def search_world_cup(edition):
    for cup in world_cups:
        if cup["edition"] == edition:
            return cup
            
    return None
