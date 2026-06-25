import random
print("===Number Guessing Game===")
print("mi 1te 100 madhla no vichar kelay... pakad bgu!")

number=random.randint(1,100)
tries=0

while True:
    guess=int(input("tuza Guess Kay ahe?"))
    tries=tries+1

    if guess< number:
       print("khup lahan aahe! Motha number sang!")
     elif guess>number:
         print("khoob Mota aahe! lahan number sang!")
       else:
            print(f"shabash tai!{tries} pretnat pakadlas!")
            print(f"no hota:{number}") 
            break 
