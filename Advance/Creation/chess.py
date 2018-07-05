class ChessCoordinate:
    def __new__(cls, *args, **kwargs):
        print("args = ", repr(args))
        print("kwargs = ", repr(kwargs))
        obj = super().__new__(cls)
        print("id(obj) = ", id(obj))
        return obj
    
    def __init__(self, file, rank):
        
        print("id(self) = ", id(self))

        if len(file) != 1:
            raise ValueError("{} compoment file {!r} does not have a length of one.".format(
                self.__class__.__name__, file
            ))
        """
        TODO: more code here
        """
        
