from random import randint

from FrogsGenerator import FrogsGenerator
from SilverGenerator import SilverGenerator
from GoldGenerator import GoldGenerator
from OldThingsGenerator import OldThingsGenerator


if __name__ == '__main__':
    fabricList = [GoldGenerator(), SilverGenerator(), OldThingsGenerator(), FrogsGenerator()]
    for i in range(20):
        chest = fabricList[randint(0, 3)].create_item().open()