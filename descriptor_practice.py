# class Grade:
#     def __init__(self):
# 	    self._value = 0
     
#     def __get__(self, instance, instance_type):
#         return self._value
    
#     def __set__(self, instance, value):
#         if not (0 <= value <= 100):
#             raise ValueError("number should be between 0 and 100")
        
#         self._value = value
        
        
class Grade:
    def __init__(self):
	    self._instances = {}
     
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._instances.get(instance, 0)
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("number should be between 0 and 100")
        
        self._instances[instance] = value
        
class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


# first_exam = Exam()
# first_exam.writing_grade = 50

# second_exam = Exam()
# second_exam.writing_grade = 70
# print(second_exam.writing_grade)

class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0
        
    @property
    def writing_grade(self):
        return self._writing_grade
    
    @writing_grade.setter
    def writing_grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError("number should be between 0 and 100")
        self._writing_grade = value
        
    @property
    def math_grade(self):
        return self._math_grade
    
    @math_grade.setter
    def math_grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError("number should be between 0 and 100")
        self._math_grade = value
        

class SharedDataDescriptor:
    def __init__(self, initial_value):
        self.value = initial_value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value
    
    def __set__(self, instance, value):
        self.value = value
        

class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name) -> None:
        self.trace_attribute_name = trace_attribute_name
        self._name = None
        
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        self._track_change_in_value_for_instance(instance, value)
        instance.__dict__[self._name] = value
        
    def _track_change_in_value_for_instance(self, instance, value):
        self._set_default(instance)
        if self._need_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)
    
    def _need_to_track_change(self, instance, value) -> bool:
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True
        return value != current_value
    
    def _set_default(self, instance):
        instance.__dict__.setdefault(self.trace_attribute_name, [])
    
class Traveller:
    current_city = HistoryTracedAttribute(trace_attribute_name="cities_visited")
    
    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city
        
injun = Traveller(name="injun", current_city="aa")

class SavedInInstanceGrade:
    def __init__(self) -> None:
        self._name = None
        
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("grade should be between 0 and 100")
        instance.__dict__[self._name] = value
        

from weakref import WeakKeyDictionary

class SavedInWeakKeyGrade:
    def __init__(self):
	    self._instances = WeakKeyDictionary()

    def __set_name__(self, owner, name):
        self._name = name
     
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._instances[instance]
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("grade should be between 0 and 100")
        self._instances[instance] = value
        

class Exam:
    writing_grade = SavedInInstanceGrade()
    math_grade = SavedInWeakKeyGrade()
    
    def __init__(self, writing_grade, math_grade):
        self.writing_grade = writing_grade
        self.math_grade = math_grade
        
exam = Exam(writing_grade=50, math_grade=100)
