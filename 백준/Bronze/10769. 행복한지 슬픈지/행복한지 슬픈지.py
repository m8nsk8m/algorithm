a = input()


smile = a.count(":-)")
sad = a.count(":-(")

if smile == 0 and sad == 0: print("none")
elif smile > sad: print("happy")
elif smile == sad: print("unsure")
elif smile < sad: print("sad")