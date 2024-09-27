
import random
#length - length of list
#max - highest value in list
def fill_random (length, max):
  random_list = [] 
  for i in range (length): 
    random_value = random.randint(1, max) 
    random_list.append(random_value) 
  return(random_list)

import secrets
def fill_secrets(length, max):
  secrets_list = [] 
  for i in range(length): 
      secrets_value = secrets.randbelow(max) + 1  
      secrets_list.append(secrets_value) 
  return(secrets_list)

#Creates separate list that indexes
#amount of time a value shows up in O.G. list.
def count(list): 
  listLength = len(list) 
  listMax = max(list) 
  count_list = [0] * listMax 
  #i.e. everytime a 5 appears,  
  #+1 to the count_list index of [5]
  for i in range(listLength):  
    listValue = list[i] - 1 
    count_list[listValue] += 1 
  if listMax > 16:
    print("The list is too large to display")
  else:
    print(count_list)


def bubble_sort(list):
  listLength = len(list)
  for i in range(listLength):
    swapped = False#Tracks for swaps
    for j in range(0, listLength -1): #Traverses through list - 1
      if list[j] > list [j+1]: #compares neighbor elements
        list[j], list[j+1] = list[j+1], list[j] #swaps if true
        swapped = True
    if not swapped: #already sorted
      break
    
import time
def timeBubble(list):
  start_time = time.time()
  bubble_sort(list)
  end_time = time.time()
  duration = end_time - start_time
  return duration

def timeSort(list):
  start_time = time.time()
  list.sort()
  end_time = time.time()
  duration = end_time - start_time
  return duration


def main():
  print("1.1: Fill a data structure with 100 random numbers between 1 and 16 using `random`")
  print("Random list:")
  random_list_100 = fill_random(100, 16)
  print(random_list_100)

  print("\n1.2: Fill a data structure with 100 random numbers between 1 and 16 using EITHER `os` or `secrets`")
  print("Secrets list:")
  secrets_list_100 = fill_secrets(100, 16)
  print(secrets_list_100)

  print("\n1.3: Get a count of the unique numbers in each data structure")
  print("Count of # in random list:")
  count(random_list_100)
  print("Count of # in secrets list:")
  count(secrets_list_100)
  print("\n1.4: Based on the counts, does one method appear better than the other?")
  print("   The difference between these two lists seems negligible.")

  print("\n2: Run #1 again using numbers 1-65535, is 1.4. any different?")
  random_list_65535 = fill_random(100, 65535)
  secrets_list_65535 = fill_secrets(100, 65535)
  count(random_list_65535)
  count(secrets_list_65535)
  print("   Cannot necessarily tell. Check next section for answer.")
  print("\n2 deviation: Run #1 using 65535 random numbers between 1-16")
  random_list_65535 = fill_random(65535, 16)
  secrets_list_65535 = fill_secrets(65535, 16)
  count(random_list_65535)
  count(secrets_list_65535)
  print("   The difference between these two lists seems negligible.")

  print("\n3.1: Write a function to sort the list using your own code (for/while loops OR one of the sorting algorithms we\n discussed) and print the amount of time it takes to run")
  print("Bubble sort time:")
  duration_bubble_random_100 = timeBubble(random_list_100)
  print(duration_bubble_random_100, "seconds")

  print("\n3.2: Time how long it takes using .sort()")
  print("Python sort time: ")
  duration_bubble_secrets_100 = timeSort(secrets_list_100)
  print(duration_bubble_secrets_100, "seconds")

  print("\n4: Do #3 again but with a 100-element list with numbers between 1-65535, does the sorting time change?\n Is one more efficient with larger numbers?")
  random_list_100 = fill_random(100, 65535)
  print("Bubble sort time:")
  duration_bubble_random_100 = timeBubble(random_list_100)
  print(duration_bubble_random_100, "seconds")
  print("Python sort time: ")
  random_list_100 = fill_random(100, 16)
  duration_sort_random_100 = timeSort(random_list_100)
  print(duration_sort_random_100, "seconds")
  print(" .sort() once again, extremely quick over bubble.")

  print("\n5: Do #4 again, but with 500-element list, does the sorting time change? Does one method flounder on larger data sets?")
  random_list_500 = fill_random(500, 16)
  duration_bubble_random_500 = timeBubble(random_list_500)
  random_list_500 = fill_random(500, 16)
  duration_sort_random_500 = timeSort(random_list_500)
  print("Bubble sort time:")
  print(duration_bubble_random_500, "seconds")  
  print("Python sort time: ")
  print(duration_sort_random_500, "seconds")
  print(" .sort() seems to be over all more efficent.")

  
main()