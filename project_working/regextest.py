

import re

def main():
    print(commands(input("What's next?: ").rstrip().lower()).upper())




def commands(b):

    match = re.search(r'^(go )?(north ?east\b|north ?west\b|south ?east\b|south ?west\b|north\b|south\b|east\b|west\b|ne\b|nw\b|se\b|sw\b|n\b|s\b|e\b|w\b)$', b)
    match1 = re.search(r'^(get|drop|examine)()?(.+)?$', b)
    #call = re.search(r'^(call )$', b)
    call = re.search(r'^(call )(chemical chris\b|chris\b|fast eric\b|eric\b|big bev\b|bev\b|fat bob\b|bob\b)$', b)
    if match:
        return b
    elif match1:
        return b
    elif call:
        return b
    else:
        print("I don't understand")
        exit()





main()
