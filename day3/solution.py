DIGITS = "0123456789"

def multiply(s: str) -> int:
  if(s[0] != '('):
    return 0
  i = 1
  first_num = ""
  while s[i] in DIGITS:
    first_num += s[i]
    i += 1
  if first_num == "":
    return 0
  if s[i] != ',':
    return 0
  i += 1
  second_num = ""
  while s[i] in DIGITS:
    second_num += s[i]
    i += 1
  if s[i] != ')':
    return 0
  return int(first_num) * int(second_num)


def partOne():
  txt = ""
  with open("input.txt", "r") as f:
    txt = f.read()
  tokens = txt.split("mul")
  acc = 0
  for token in tokens:
    acc += multiply(token)
  print(acc)


def partTwo():
  txt = ""
  with open("input.txt", 'r') as f:
    txt = f.read()
  i = 0
  do = True
  acc = 0
  for i in range(len(txt)):
    if (txt[i] == 'd' and i + 5 < len(txt)):
      if (txt[i:i+7] == "don't()"):
        do = False
      elif(txt[i:i+4] == "do()"):
        do = True
    elif (txt[i] == "m" and i + 3 < len(txt) and do):
      if (txt[i:i+3] == "mul"):
        acc += multiply(txt[i+3:])
  print(acc)

def main():
  #partOne()
  partTwo()

if __name__ == "__main__":
  main()