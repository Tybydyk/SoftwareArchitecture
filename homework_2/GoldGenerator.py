from ItemFabric import ItemFabric
from ChestOfGold import ChestOfGold

class GoldGenerator(ItemFabric):

    def create_item(self):
        print("Created a chest of gold")
        return ChestOfGold()