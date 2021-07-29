from abc import ABCMeta


class MyProgram:
    def __init__(self):
        self._search_button = SearchButton()
        
    def set_search_all(self):
        self._search_button.set_search_strategy(SearchStrategyAll)
        
    def set_search_image(self):
        self._search_button.set_search_strategy(SearchStrategyImage)
                
    def set_search_news(self):
        self._search_button.set_search_strategy(SearchStrategyNews)
                
    def set_search_map(self):
        self._search_button.set_search_strategy(SearchStrategyMap)
        
    def test_program(self):
        self._search_button.on_click()
        
        self.set_search_all()
        self._search_button.on_click()     
           
        self.set_search_image()
        self._search_button.on_click()
        
        self.set_search_news()
        self._search_button.on_click()

        self.set_search_map()
        self._search_button.on_click()
        
        
class SearchStrategy(metaclass=ABCMeta):
    def search(self):
        raise NotImplementedError()
    
class SearchStrategyAll(SearchStrategy):
    def search(self):
        print("search ALL")

class SearchStrategyImage(SearchStrategy):
    def search(self):
        print("search Image")

class SearchStrategyNews(SearchStrategy):
    def search(self):
        print("search News")
        
class SearchStrategyMap(SearchStrategy):
    def search(self):
        print("search Map")
            
class SearchButton:
    def __init__(self):
        self.set_search_strategy(SearchStrategyAll)
    
    def set_search_strategy(self, search_stragegy: SearchStrategy):
        self._search_stragy = search_stragegy()
        
    def on_click(self):
        self._search_stragy.search()
        
          
MyProgram().test_program()