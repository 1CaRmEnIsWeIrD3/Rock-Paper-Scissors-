import random


intro=print ("Rock, paper, scissors!")
escolhaplayer1=input("Player 1: (choose rock, paper or scissors): ").lower()
escolhaplayer2=random.choice(['paper', 'rock','scissors'])
print(f"Imaginary Friend: {escolhaplayer2}")

if escolhaplayer1=="rock" and escolhaplayer2=="rock"or escolhaplayer1=="paper" and escolhaplayer2=="paper"or escolhaplayer1=="scissors" and escolhaplayer2=="scissors":
    print("Draw")
elif escolhaplayer1=="rock" and escolhaplayer2=="scissors"or escolhaplayer2=="rock" and escolhaplayer1=="paper":
    print("Player 1 wins!")
elif escolhaplayer1=="rock" and escolhaplayer2=="paper"or escolhaplayer2=="rock" and escolhaplayer1=="scissors":
    print("Player 2 wins!")

else:
    print("Hey, are you ok? It's not that hard. Try again!")
