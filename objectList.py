class objectList():
    def __init__(self, type:str=None):
        self.type = type
        self.count = 0
        self.objects = {}
    
    def createObject(self, object):
        self.objects[self.count] = object
        self.count += 1
        return object
    
    def removeObject(self, id):
        del self.objects[id]
    
    def removeObjects(self, ids):
        ids = sorted(ids, reverse=True)

        for id in set(ids):
            self.removeObject(id)
    
    def getObject(self, id):
        return self.objects[id]
    
    def getAllObjects(self):
        return self.objects
    
    def setObject(self, id, object):
        self.objects[id] = object
        return self.objects[id]
    
    def update(self, game):
        for object in self.objects.values():
            object.update(game)
    
    def draw(self, game):
        for object in self.objects.values():
            object.draw(game)
    
    def wipe(self):
        self.objects = {}