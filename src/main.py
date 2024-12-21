from Manager import Manager
from EpicGamesModule import EpicGamesModule

m = Manager()
a = EpicGamesModule("Epic Games Store check")
m.add_modules([a])
m.run()
m.quit()
