"""
Proxy

An interface for accessing a particular resources

You are calling foo.Bar()
This assumes that foo is in the same process as Bar()
What if, later on, you want to put all Foo-related operations into a separate process
    - Can you avoid changing your code?
Proxy to the rescue!
    - Same interface, entirely different behavior
This is called a communication proxy
    - Other types: logging, virtual, guarding

PROXY -> A class that functions as an interface to a particular resources.
That resources may be remote, expensive to construct, or may require logging or some other added functionality


Proxy vs. Decorator
Proxy provides an identical interface; decorator provides an enhanced interface
Decorator typically aggregates (or has reference to) what it is decorating; proxy doesn't have to
Proxy might not even be working with a materialized object

Summary
A proxy has the same interface as the underlying object
To create a proxy, simply replicate the existing interface of an object
Add relevant functionality to the redefined member functions
Different proxies (communication, logging, caching,...) have completely different behaviours


"""


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


car = CarProxy(Driver("Omer", 38))
car.drive()
