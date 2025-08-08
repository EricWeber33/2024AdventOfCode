# solution by Eric Weber
# a previous solution found the correct answer based on the input provided 
# by advent of code but was incorrect for [[10, 9, 8, 7, 100]]
# this latest version is correct for all input as well as the above 'extra' input

def load_input() -> list[list[int]]:
  reports = []
  with open("input.txt", "r") as file:
    for line in file.readlines():
      reports.append([int(x) for x in line.split()])
  return reports
 

def is_decreasing(l: list[int]) -> bool:
  decrease_count = 0
  increase_count = 0
  for i in range(len(l)):
    if l[i] > 0:
      increase_count += 1
    elif l[i] < 0:
      decrease_count += 1
  return decrease_count > increase_count

def diffs_valid(l: list[int], depth = 0) -> bool:
  if (is_decreasing(l)):
    # flips signs of differences, 
    # this is mostly because it makes it easier
    # for me to reason about what to do next
    # and also has no effect on the result
    l = [x*-1 for x in l]
  for i in range(len(l)):
    if not (1 <= l[i] and l[i] <= 3):
      if (depth > 0):
        return False
      # add bad diff to adjacent diffs and try again
      if (i == len(l) - 1):
        l1 = l[:-1]
        l2 = [l[-1] + l[-2]] + l[:-2]
        return diffs_valid(l[:-1], depth+1) or diffs_valid(l2, depth+1)
      elif (i == 0):
        l1 = l[1:]
        l2 = [l[0] + l[1]] + l[2:]
        return diffs_valid(l[1:], depth+1) or diffs_valid(l2, depth+1)
      else:
        l1 = l[:i] + [l[i] + l[i+1]] + l[i+2:]
        l2 = l[:i-1] + [l[i-1]+ l[i]] + l[i+1:]
        return diffs_valid(l1, depth+1) or diffs_valid(l2, depth+1)     
  return True

def is_safe(report: list[int]) -> bool:
  # part one solution
  # assert len(report) >= 1
  # previous = report[0]
  # current = report[1]
  # sign = 1 if current > previous else -1
  # diff = (current - previous) * sign
  # if not (1 <= diff and diff <= 3):
  #   return False
  # previous = current
  # for current in report[2:]:
  #   diff = (current - previous) * sign
  #   if not (1 <= diff and diff <= 3):
  #     return False
  #   previous = current
  # return True
  assert len (report) >= 1
  diff_list = []
  for i in range (1, len(report)):
    diff_list.append(report[i] - report[i-1])
  return diffs_valid(diff_list)
  

def main():
  total_safe = 0
  for x in load_input():
    if is_safe(x):
      total_safe += 1
  print( total_safe )

if __name__ == "__main__":
  main()