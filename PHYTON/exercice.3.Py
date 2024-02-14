

def NULL_not_found(value):
  if value is None:
      return "NULL"
  else:
      return "Not NULL"


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

print(NULL_not_found(Nothing))
print(NULL_not_found(Garlic))
print(NULL_not_found(Zero))
print(NULL_not_found(Empty))
print(NULL_not_found(Fake))
print(NULL_not_found("Brian"))