from ItemFabric import ItemFabric
from ChestOfSilver import ChestOfSilver

class SilverGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest of silver")
        return ChestOfSilver()