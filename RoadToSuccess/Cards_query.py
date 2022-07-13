"""QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
 Write a function to help Bob locate the card.
 
 
 We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
  We also need to minimize the number of times we access elements from the list.

Input
cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
query: A number, whose position in the array is to be determined. E.g. 7
Output
position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)"""



# Brute force approach (linear search)

def locate_cards(cards,queries):
    position = 0

    while position < len(cards):
        if cards[position] == queries:
            return position
        position+=1

     
    return -1


cards = list(map(int,input().split()))
queries = int(input())
result = locate_cards(cards,queries)
print(result)
