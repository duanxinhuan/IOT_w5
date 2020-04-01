# Reference: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class Singleton:
    __instance = None
    #this is very similer to static in java

    @staticmethod
    def getInstance():
        if(Singleton.__instance == None):
            Singleton()
            #initialize a instance here
        return Singleton.__instance

    def __init__(self):
        if(Singleton.__instance != None):
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            #when initialize , its instance is itself, then can't raise a instance of it

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

s=Singleton()

# if it is static :VARIABLE
#if it belongs to instance _variable
#if private __variable
# if private def __getName()