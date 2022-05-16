class MyObject:
    pass
    int_field = 9 #атрибут класа
    str_field = 'a string' #атрибут класа
print(MyObject.int_field)
print(MyObject.str_field)
object1=MyObject
object2=MyObject
MyObject.int_field
object1.int_field
print(object1.int_field)
print(object2.str_field)

