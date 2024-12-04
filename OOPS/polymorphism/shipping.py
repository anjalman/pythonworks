
class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*20)

class StandardShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*10)

express_Shipping_instance=ExpressShipping()

express_Shipping_instance.calculate_shipping_cost(10)

shipping_instance=Shipping()

shipping_instance.calculate_shipping_cost(5)

StandardShipping_instance=StandardShipping()

StandardShipping_instance.calculate_shipping_cost(5)

