#практическая работа 17.Вариант 6
# вывести список сданных предметов

from itertools import compress
class Student:
        items=['english','biology','geography','maths','computer Science','music']
        result=[True,True,False,True,False,True]
        def passExam(self):
            return list(compress(self.items,self.result ))
res=Student()
print(res.passExam())
                