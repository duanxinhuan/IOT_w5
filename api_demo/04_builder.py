# Reference: https:#code.msdn.microsoft.com/windowsapps/Design-Patterns-Builder-26d38c45
# Adapted into python code.
from abc import ABC, abstractmethod

# Product - The main object that will be created by the Director using Builder.
class Pizza:
    def __init__(self):
        self.sauce = ""
        self.topping = ""

# Builder - Abstract interface for creating objects (the product).
class PizzaBuilder(ABC):
    def __init__(self):
        self._pizza = None

    def GetPizza(self):
        return self._pizza
    
    def CreateNewPizzaProduct(self):
        self._pizza = Pizza()

    @abstractmethod
    def BuildSauce(self):
        pass
    
    @abstractmethod
    def BuildTopping(self):
        pass

# Concrete Builder - Provides implementation for Builder An object able to construct other objects.
# Constructs and assembles parts to build the objects.
class CheesePizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def BuildSauce(self):
        self._pizza.Sauce = "Cheese"

    def BuildTopping(self):
        self._pizza.Topping = "Green Pepper"

# Concrete Builder - Provides implementation for Builder An object able to construct other objects.
# Constructs and assembles parts to build the objects.
class SpicyPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()
    
    def BuildSauce(self):
        self._pizza.Sauce = "Hot Sauce"

    def BuildTopping(self):
        self._pizza.Topping = "Red Pepper, Jalapeno"

# Director - Responsible for managing the correct sequence of object creation.
# Receives a Concrete Builder as a parameter and performs the necessary operations on it.
class Cook:
    def __init__(self):
        self.__pizzaBuilder = None

    # Step 1. Construct the builder object for the given concrete object.
    def SetPizzaBuilder(self, pizzaBuilderObject):
        self.__pizzaBuilder = pizzaBuilderObject

    # Step 2. Call required methods from the builder class.
    # Step 3. Call required methods from the concrete builder classes.
    def ConstructPizza(self):
        # Calling builder object's method.
        self.__pizzaBuilder.CreateNewPizzaProduct()

        # Calling Concrete object's methods.
        self.__pizzaBuilder.BuildSauce()
        self.__pizzaBuilder.BuildTopping()

    # Step 4. Return the product after creating it based on the builder and concrete objects.
    def GetPizza(self):
        return self.__pizzaBuilder.GetPizza()

# 1. Create an instance for Builder and initialize with Concrete builder - CheesePizzaBuilder.
cheesePizzaBuilder = CheesePizzaBuilder()

# 2. Create an instance for Director.
cook = Cook()

# 3. By using Director instance, call the concrete object methods.
cook.SetPizzaBuilder(cheesePizzaBuilder)
cook.ConstructPizza()

# 4. Create and get the product, by using the Director.
cheesePizzaProduct = cook.GetPizza()

# 5. Deliver the product.
print("Cheese Pizza prepared by using {} and {}".format(cheesePizzaProduct.Topping, cheesePizzaProduct.Sauce))

# 1. Create an instance for Builder and initialize with Concrete builder - SpicyPizzaBuilder.
spicyPizzaBuilder = SpicyPizzaBuilder()

# 2. Use same Director instance.
# 3. And pass the new concrete Builder instance.
cook.SetPizzaBuilder(spicyPizzaBuilder)
cook.ConstructPizza()

# 4. Create and get the product, by using the Director.
spicyPizzaProduct = cook.GetPizza()

# 5. Deliver the product.
print("Spicy Pizza prepared by using {} and {}".format(spicyPizzaProduct.Topping, spicyPizzaProduct.Sauce))
