from math import sqrt

def is_prime( x ):
  if x == 2: return True
  if x < 2 or x % 2 == 0 : return False

  for value in range( 3, int( sqrt(x) ) + 1, 2 ):
    if x % value == 0: return False

  return True
