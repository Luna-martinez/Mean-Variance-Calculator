import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  array = np.array(list).reshape((3, 3))
  calculations = {
    "mean": [
      np.mean(array, axis = 0).tolist(),
      np.mean(array, axis = 1).tolist(),
      np.mean(array.tolist())
    ],
    "variance": [
      np.var(array, axis = 0).tolist(),
      np.var(array, axis = 1).tolist(),
      np.var(array) .tolist()    
    ],
    "standard deviation": [
      np.std(array, axis = 0).tolist(),
      np.std(array, axis = 1).tolist(),
      np.std(array).tolist()     
    ],    
  }

  return calculations