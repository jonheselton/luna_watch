# from app_luna_watch.models import Schedule
# s = Schedule.objects.first()

class MyClass:
    def __init__(self, *args, **kwargs):
        self.a = list(range(1,10))


class MyClass2(MyClass):
    def __init__(self, *args, **kwargs):
        super(MyClass2, self).__init__(self)
        self.a += list(range(100, 110))



from app_luna_watch.models import Schedule, Visit, Visitor


a = Schedule.objects.first()
v = Visitor.objects.first()

