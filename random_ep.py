"""
Use for selecting a random season and episode of a TV series

"""


import random

def get_season():

    m = int(input("Enter number of lower limit season: "))
    n = int(input("Enter number of upper limit season: "))
    
    s = random.randint(m, n)

    print("Season: " + str(s))

def get_episode():

    c = int(input("Enter number of lower limit episode: "))
    d = int(input("Enter number of upper limit episode: "))
    
    ep = random.randint(c, d)

    print("Episode: " + str(ep))


def pick_ep_n_season():

    get_season()
    get_episode()


pick_ep_n_season()


