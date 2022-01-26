class mobile:
    fp='Yes'
    @classmethod
    def name(cls,string):
        cls.fp=string
        print(cls.fp)
n=mobile()
n.name('no')
mobile.fp
