class Dog(object):
    def work(self):
        print('指哪打哪')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, x):
        x.work()


d = Dog ()
ad = ArmyDog()
dd = DrugDog()
liu = Person()
liu.work_with_dog(d)
liu.work_with_dog(ad)
liu.work_with_dog(dd)


class Pensile():
    def work(self):
        print('写铅笔字')


class Pen():
    def work(self):
        print('写钢笔字')


class People():
    def write(self, p):
        p.work()


jiankang = People()
pensile = Pensile()
pen = Pen()
jiankang.write(pensile)
jiankang.write(pen)




