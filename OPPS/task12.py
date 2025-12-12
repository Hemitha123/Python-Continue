#Multiple Inheritance 

class steptracker():
    def __init__(self,steps):
        self.steps=steps
    
    def calories_burned(self):
        self.cal=self.steps*0.04
        
class sleeptracker():
    def __init__(self,hours_slept):
        self.hours_slept=hours_slept
    def sleep_score(self):
        self.sc=self.hours_slept*10
        
class healthreport(steptracker,sleeptracker):
    def __init__(self,steps,hours_slept):
        steptracker.__init__(self,steps)              #called parent1(steptracker)
        sleeptracker.__init__(self,hours_slept)       #called parent2(sleeptracker)

    def daily_report(self):
        print(f"The calories burnt is:{self.cal}")
        print(f"The sleep score is:{self.sc}")
h1=healthreport(10000,8)
h1.calories_burned()
h1.sleep_score()
h1.daily_report()
