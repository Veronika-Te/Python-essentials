#--->Aggregation

#Objects are linked as parts of a larger structure, 
# but can live independently
class File:
    def __init__(self, name):
        self.name = name

class Folder:
    def __init__(self):
        self.files = []  # Aggregation

    def add_file(self, file):
        self.files.append(file)

file1 = File("report.pdf")
file2 = File("image.png")

folder = Folder()
folder.add_file(file1)
folder.add_file(file2)

for f in folder.files:
    print(f.name)
    
#--->Server
class TrafficLightServer:
    def __init__(self, color):
        self.color = color

    def get_state(self):
        return self.color

class Car:
    def __init__(self, brand, server):
        self.brand = brand
        self.server = server  # Car depends on server

    def move(self):
        light = self.server.get_state()
        if light == "Green":
            print(f"{self.brand} drives.")
        else:
            print(f"{self.brand} waits at {light} light.")

server = TrafficLightServer("Red")
car = Car("Toyota", server)
car.move()


#--->Controller
#The TrafficController manages how Drivers interact with their Cars and respond to TrafficLight.
class TrafficLight:
    def __init__(self, color):
        self.color = color

    def is_green(self):
        return self.color.lower() == "green"

class Car:
    def drive(self):
        print("Car is driving...")

class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

class TrafficController:
    def __init__(self, driver, traffic_light):
        self.driver = driver
        self.traffic_light = traffic_light

    def manage(self):
        print(f"{self.driver.name} is waiting for signal...")
        if self.traffic_light.is_green():
            self.driver.car.drive()
        else:
            print("Wait! Traffic light is red.")

light = TrafficLight("Green")
car = Car()
driver = Driver("Alice", car)
controller = TrafficController(driver, light)
controller.manage()



