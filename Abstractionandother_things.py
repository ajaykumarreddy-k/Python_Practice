#anstraction in python
class car():
    def start(self):
        print("Car started")
    def drive(self):
        print("Car is driving")
    def __engine_process(self):
        print("Fuel injrction , combustion,piston moving")
    def run(self):
        self.__engine_process()
        print("Car is running")
c1 = car()
c1.start()
c1.drive()
c1.run()
#Class with multiple constructor methods and a best example for abstraction in python
# Remaining check google colab link .