class course:
    def __init__(self,c_name,stud_list):
        self.__c_name=c_name
        self.__stud_list=stud_list
    def get_cname(self):
        return self.__c_name
    def get_slist(self):
        return self.__stud_list
    def add_stud(self,name):    #adds if name not in list 
        if name not in self.__stud_list:
            self.__stud_list.append(name)
            return f"{name} added successfully"
        else:
            return f"{name} already exists"
    def remove_stud(self,name):     #removes if name is in list
        if name in self.__stud_list:
            self.__stud_list.remove(name)
            return f"{name} is removed successfully"
        else:
            return f"{name} not found"
s1=course("Python",["Ram"])
print(f"Course is:{s1.get_cname()}")
print(f"Student list:{s1.get_slist()}")
s1.add_stud("Sham")
print(s1.get_slist())
s1.remove_stud("Sam")
print(s1.get_slist())