from pathlib import Path

# path = Path("pythonCoding/chapter10/pi_digits.txt")
# contents = path.read_text()
# contents = contents.rstrip()
# print(contents)

# 访问文件中的各行
path = Path("pythonCoding/chapter10/pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
