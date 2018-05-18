def how_many(dictionary):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: int, how many values are in the dictionary.
  '''
  how_many = 0
  for key in dictionary:
      how_many += len(dictionary[key])
  return how_many

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'] }
print(animals)
print('there are ' + str(how_many(animals)) + ' animals in animals')

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo'], 'e': ['elephant', 'egg'] }
print(animals)
print('there are ' + str(how_many(animals)) + ' animals in animals')
print('\n')