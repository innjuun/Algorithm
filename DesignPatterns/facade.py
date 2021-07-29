class GeoLocation:
    def get_loc(self):
        self.geo_loc = (0, 0)
        return self.geo_loc
    
class InternetConnection:
    def connect(self):
        pass
    
    def get_data(self, url):
        return ""
    
    def disconnect(self):
        pass
    
class Json:
    def parse(self, value):
        return {"address": "종혁동 범수구"}

class MyLocFacade:
    def print_my_address(self):
        self.geo_loc = GeoLocation().get_loc()
        connection = InternetConnection()

        connection.connect()
        data = connection.get_data("http://dummy.com", self.geo_loc)
        connection.disconnect()
        
        address = Json().parse(data)
        print(address["address"])
        
        
MyLocFacade().print_my_address()