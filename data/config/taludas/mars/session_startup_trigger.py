session.startSequence(5)

import random

# Your list of numbers
numbers = [19990315, 19990319, 19990322, 19990325, 19990328, 19990331, 19990334, 19990337, 19990340, 19990343]

# Select a random number from the list
random_number = random.choice(numbers)

exec("debug.toggleSectorEffect({})".format(random_number))

quests.startQuest(19990383)