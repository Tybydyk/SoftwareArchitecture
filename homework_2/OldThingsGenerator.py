from ItemFabric import ItemFabric
from ChestOfOldThings import ChestOfOldThings

class OldThingsGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest of Old Things")
        return ChestOfOldThings()