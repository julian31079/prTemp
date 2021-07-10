class Temp:
    def __init__(self,setPoint):
        self.setPoint=setPoint
    def control(self,value):
        if(value<self.setPoint):
            return True
        else:
            return False