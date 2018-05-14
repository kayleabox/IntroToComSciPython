def biggest(dictionary):
  biggest = None
  for key in dictionary:
    if biggest == None:
      biggest = key
    elif len(dictionary[key]) > len(dictionary[biggest]):
      biggest = key
  return biggest
