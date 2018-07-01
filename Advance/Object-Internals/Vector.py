# class Vector:

#     def __init__(self, **coords):
#         # auto add attributes follow list in the coords
#         # alter define attribute manual
#         self.__dict__.update(coords)
    
#     def __repr__(self):
#         return "{}({})".format(
#             self.__class__.__name__,
#             ', '.join("{k}={v}".format(
#                 k = k,
#                 v = self.__dict__[k])
#                 for k in sorted(self.__dict__.keys())
#             )
#         )

class Vector:

    def __init__(self, **coords):
        private_coords = {'_'+ k : v for k,v in coords.items()}
        # auto add attributes follow list in the coords
        # alter define attribute manual
        self.__dict__.update(private_coords)
    
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k = k[1:],
                v = self.__dict__[k])
                for k in sorted(self.__dict__.keys())
            )
        )
    