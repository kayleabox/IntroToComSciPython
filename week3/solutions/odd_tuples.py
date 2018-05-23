'''
Write a procedure called oddTuples, which takes a tuple as input,
and returns a new tuple as output, where every other element of 
the input tuple is copied, starting with the first one. So if test 
is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating 
oddTuples on this input would return the tuple ('I', 'a', 'tuple')
'''

def odd_tuples(old_tuple):
  new_tuple = ()
  for i in range(0, len(old_tuple), 2):
    new_tuple += (old_tuple[i], )
  return new_tuple

print('odd_tuples:')
old_tuple = ('socks', 'shoes', 'apples', 'bananas', 1, 2, 3)
print('old tuple: ' + str(old_tuple) + ' new tuple' + str(odd_tuples(old_tuple)))
print('\n')