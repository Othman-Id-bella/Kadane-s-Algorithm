def kadane(MyList):
  max_sum = 0
  current_sum = 0
  for i in MyList: 
    current_sum = current_sum + i
    if current_sum < 0:
      current_sum = 0
    if max_sum < current_sum:
      max_sum = current_sum
  return max_sum