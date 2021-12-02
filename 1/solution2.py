file = open('input.txt', 'r')
lines = file.readlines()

increases = 0

for i in range(3, len(lines)):
  old_depth = int(lines[i-3])
  new_depth = int(lines[i])
  if new_depth > old_depth:
    increases += 1

print(increases)