def how_many(dictionary):
  how_many = 0
  for key in dictionary:
      how_many += len(dictionary[key])
  return how_many