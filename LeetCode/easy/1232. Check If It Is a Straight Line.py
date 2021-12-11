class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        self.before_slide = None
        
        for i, (x, y) in enumerate(coordinates):
            if i == 0:
                self.before_x = x
                self.before_y = y
                continue
            
            if x - self.before_x == 0:
                new_slide = 0
            elif y - self.before_y == 0:
                new_slide = 10000
            else:
                new_slide = (x - self.before_x) / (y - self.before_y)
            if self.before_slide is not None:
                # print(self.before_slide)
                if self.before_slide != new_slide:
                    return False
            self.before_slide = new_slide
            self.before_x = x
            self.before_y = y
            
        return True
            