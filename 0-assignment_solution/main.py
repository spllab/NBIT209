# Author PAUL OFFEI
# Date: 4/10/2023
# Program Description: Testing our Sorting Algorithm

from sorting import insertion_sort, insertion_sorted, selection_sort, selection_sorted, bubble_sort, bubble_sorted 


numbers = [2,1,4,5,3]
play_cards = [8,7,2,4,10,3]


print("-------------Bubble Sorted-----------")
print(play_cards)
print(bubble_sorted(play_cards))
print(play_cards)
print("================================================================")
print("-------------Bubble Sort-----------")
print(play_cards)
bubble_sort(play_cards)
print(play_cards)
print("================================================================")
print("--------Selection Sorted--------------------")
print(play_cards)
print(selection_sorted(play_cards))
print(play_cards)
print("=================================================================")

print("-------------Selection Sort----------------")
print(numbers)
selection_sort(numbers)
print(numbers)
print("=======================================================================")

print("-------------Insertion Sort------------------")
print(numbers)
print(insertion_sort(numbers))
print(numbers)
print("=====================================================")

print("------------Insertion Sorted--------------------")
print(play_cards)
play = insertion_sorted(play_cards)
print(play)
print(insertion_sorted(play_cards))
print(play_cards)
