from sometime import Sometime

test = Sometime().from_iso("2021-01-15", "%Y-%m-%d")
print(test.timestamp())