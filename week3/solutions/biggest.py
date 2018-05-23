def biggest(dictionary):
  '''
  aDict: A dictionary, where all the values are lists.
  returns: The key with the largest number of values associated with it
  '''
  biggest = None
  for key in dictionary:
    if biggest == None:
      biggest = key
    elif len(dictionary[key]) > len(dictionary[biggest]):
      biggest = key
  return biggest

def biggest2(dictionary):
  return max({key:len(value) for key,value in dictionary.items()}.keys())

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'] }
print(animals)
print('the biggest list in the dicitonary is: ' + str(biggest(animals)))
print('the biggest list in the dicitonary is: ' + str(biggest2(animals)))    

dictionary = {}
print(dictionary)
print('the biggest list in the dicitonary is: ' + str(biggest(dictionary)))
print('\n')
