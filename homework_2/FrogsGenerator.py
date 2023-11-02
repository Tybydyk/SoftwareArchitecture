from ItemFabric import ItemFabric
from ChestOfFrogs import ChestOfFrogs

class FrogsGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest of frogs")
        return ChestOfFrogs()