import random
from random_word import RandomWords
import time
r = RandomWords()
while True:
    time.sleep(5)
    try:
        word1 = r.get_random_word(maxLength=4, minLength=4)
        word2 = r.get_random_word(maxLength=4, minLength=4)
    except:
        print('error getting words, starting over')
        print('starting exception delay')
        time.sleep(10)
        print('exception delay, done 5secs till actual word request, since delay')
    else:
        num = random.randint(1, 9)
        passw = int(word1) + int(word2) + int(num)
        print(passw)
