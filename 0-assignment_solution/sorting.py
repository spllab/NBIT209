# Author PAUL OFFEI
# Date: 4/10/2023
# Program Description: Implementation of Basic Sorting Algorithm as Functions


def insertion_sort(number_cards):
    """
    Behaviour::Interface::Specification
    Takes in an array of items and sort them in place.
    
    PreCondiction:: Takes Unsorted array of items [2,1,3,5,4] 

    PostCondition:: Sort the array of items in place [1,2,3,4,5]
    """
    for i in range(1, len(number_cards)):
        j = i - 1
        while j >= 0 and number_cards[j] > number_cards[j+1]:
            temp = number_cards[j]
            number_cards[j] = number_cards[j+1]
            number_cards[j+1] = temp 
            j -= 1
    return number_cards


def insertion_sorted(cards):
    """
    Behaviour::Interface::Specification
    Takes in an array of items and sort it and return a new sorted array.
    
    PreCondiction:: Takes Unsorted array of items [2,1,3,5,4] 

    PostCondition:: Sort the array of items in place => [1,2,3,4,5]
    """
    number_cards = list(cards)
    for i in range(1, len(cards)):
        j = i - 1
        while j >= 0 and number_cards[j] > number_cards[j+1]:
            temp = number_cards[j]
            number_cards[j] = number_cards[j+1]
            number_cards[j+1] = temp 
            j -= 1

    return number_cards


def selection_sort(number_cards):
    """
    Behaviour::Interface::Specification
    Takes in an array of items and sort it in place.
    
    PreCondiction:: Takes Unsorted array of items [2,1,3,5,4] 

    PostCondition:: Sort the array of items in place => [1,2,3,4,5]
    """
    
    for i in range(len(number_cards)):
        index_with_minimum = i
        for j in range(index_with_minimum+1, len(number_cards)):
            if number_cards[j] < number_cards[index_with_minimum]:
                index_with_minimum = j
        temp = number_cards[i]
        number_cards[i] = number_cards[index_with_minimum]
        number_cards[index_with_minimum] = temp 

    return number_cards 

def selection_sorted(number_cards):
    cards = list(number_cards)
    """
    Behaviour::Interface::Specification
    Takes in an array of items and sort it and return a new sorted array.
    
    PreCondiction:: Takes Unsorted array of items [2,1,3,5,4] 

    PostCondition:: Sort the array of items in place => [1,2,3,4,5]
    """
    
    for i in range(len(cards)):
        index_with_minimum = i
        for j in range(index_with_minimum+1, len(cards)):
            if cards[j] < cards[index_with_minimum]:
                index_with_minimum = j
        temp = cards[i]
        cards[i] = cards[index_with_minimum]
        cards[index_with_minimum] = temp 

    return cards 


def bubble_sort(number_cards):
    """
    Behaviour::Interface::Specification
    Takes in an array of items and sort it in place.
    
    PreCondiction:: Takes Unsorted array of items [2,1,3,5,4] 

    PostCondition:: Sort the array of items in place => [1,2,3,4,5]
    """

    for i in range(len(number_cards)-1):
        swap_counter = 0
        for j in range(len(number_cards) - i -1):
            if number_cards[j] > number_cards[j+1]:
                swap_counter += 1
                number_cards[j], number_cards[j+1] = number_cards[j+1], number_cards[j]
        if swap_counter == 0:
            return number_cards
    return number_cards


def bubble_sorted(number_cards):
    cards = list(number_cards)
    """
    Behaviour::Interface::Specification
    Takes in an array of items and sort it and return a new sorted array.
    
    PreCondiction:: Takes Unsorted array of items [2,1,3,5,4] 

    PostCondition:: Sort the array of items in place => [1,2,3,4,5]
    """

    for i in range(len(cards)-1):
        swap_counter = 0
        for j in range(len(cards) - i -1):
            if cards[j] > cards[j+1]:
                swap_counter += 1
                cards[j], cards[j+1] = cards[j+1], cards[j]
        if swap_counter == 0:
            return cards
    return cards


