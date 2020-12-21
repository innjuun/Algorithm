import json

class Serializable:
    def __init__(self, *args):
        self.args = args
        
    
    def serialize(self):
        return json.dumps({"args": self.args})
    
    
class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        

class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])    
    
class BetterPoint2D(Deserializable):
    pass
point = Point2D(5,3)
a = point.serialize()
b = BetterPoint2D.deserialize(a)
print(b)