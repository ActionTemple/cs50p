

# Deep Thought
# Andrew Waddington


answer = input("What is the answer to the great question of life, the universe, and everything? ")
answerb = answer.lower()
answerc = answerb.strip()

match answerc:
    case "42"|"forty-two"|"forty two":
        print ("Yes")
    case _:
        print ("No")

