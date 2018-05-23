def how_many(dictionary):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: int, how many values are in the dictionary.
  '''
  return sum([len(dictionary[key]) for key in dictionary])

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'] }
print(animals)
print('there are ' + str(how_many(animals)) + ' animals in animals')

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'], 'e': ['elephant', 'egg'] }
print(animals)
print('there are ' + str(how_many(animals)) + ' animals in animals')
print('\n')