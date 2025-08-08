def loadInput() -> tuple[list[int], list[int]]:
  l1 = []
  l2 = []
  with open("input.txt", "r") as f:
    for line in f.readlines():
      ln = line.split()
      l1.append(int(ln[0]))
      l2.append(int(ln[1]))
  l1.sort()
  l2.sort()
  return (l1, l2)

def partOne():
  l1, l2 = loadInput()
  acc = 0
  for i, j in zip(l1, l2):
    acc += abs(i - j)
  print(acc)

def partTwo():
  l1, l2 = loadInput()
  amount_map = {}
  similarity = 0
  for x in l2:
    if x not in amount_map:
      amount_map[x] = 1
    else:
      amount_map[x] += 1
  for x in l1:
    if x in amount_map:
      similarity += x * amount_map[x]
  print(similarity)

def main():
  #partOne():
  partTwo()

if __name__ == "__main__":
  main()