# Reference: http://msdn.microsoft.com/en-us/library/orm-9780596527730-01-04.aspx
# Adapted into python code. :)
from abc import ABC, abstractmethod

# Simplest adapter using interfaces and inheritance.

# Code Base X -> old (legacy).
# Code Base Y calls into Code Base X.
# New Code will only call Code Base Y.

# Existing way requests are implemented.
class Adaptee:
    # Provide full precision.
    def SpecificRequest(self, a, b):
        return a / b

# Required standard for requests.
class ITarget(ABC):
    # Rough estimate required.
    @abstractmethod
    def Request(self, i):
        pass

# Implementing the required standard via Adaptee.
class Adapter(Adaptee, ITarget):
    def Request(self, i):
        return "Rough estimate is {}".format(round(self.SpecificRequest(i, 3)))

# Showing the Adaptee in standalone mode - legacy code.
first = Adaptee()
print("Before the new standard.")
print("Precise reading: {}".format(first.SpecificRequest(5, 3)))

# New code.
second = Adapter()
print()
print("Moving to the new standard.")
print(second.Request(5))
