

# from CS50.ai:
answer = input("What is the answer to the great question of life, the universe, and everything? ").lower().strip()
# would be a better way of handling the input

# answer = input("What is the answer to the great question of life, the universe, and everything? ")
# answerb = answer.lower()
# answerc = answerb.strip()

match answer:
    case "42"|"forty-two"|"forty two":
        print ("Yes")
    case _:
        print ("No")

