from objectList import objectList

class objectHandler():
    def __init__(self, game):
        self.objectLists = {}
        self.game = game
    
    def update(self):
        for objectList in self.objectLists.values():
            objectList.update(self.game)
    
    def draw(self):
        for objectList in self.objectLists.values():
            objectList.draw(self.game)

    def createObjectList(self, type:str):
        self.objectLists[type] = objectList(type)
        return self.objectLists[type]
    
    def createObject(self, type:str, object):
        if type not in self.objectLists.keys():
            self.createObjectList(type)
        return self.getObjectList(type).createObject(object)

    def getObject(self, type:str, id:int):
        return self.getObjectList(type).getObject(id)

    def getObjectList(self, type:str):
        return self.objectLists[type]

    def removeObject(self, type:str, id:int):
        self.createObjectList(type).removeObject(id)
    
    
