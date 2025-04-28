from pathlib import Path
import json

path = Path("pythonCoding\\chapter10\\number.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
