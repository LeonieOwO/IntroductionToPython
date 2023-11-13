class Student:
    count = 0


    def _init_(self,name,age,matric_num):
        self.name = name
        self.age = age
        self.matric_num = matric_num
        self.__secret = "geheim" #kommt in anderen namespace weil2 _ . wird als private variable genutzt
        Student.count += 1

    @classmethod
    def add_stud(cls, name, age, matric_num):
        return cls(name, age, matric_num)

    @property  #sorgt dafür, dass ich wie auf n Attribut zugreifen kann statt get_age einfach age
    def get_age(self):
        return self._age 

    def set_age(self, age):
        if age > 0:
         self._age = age   
    
    @staticmethod
    def greet():
        return "Hello"
        

    def _str_(self):
        return f"Name: {self.name}, Age: {self.age}")
        
