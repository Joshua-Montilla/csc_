Places = ["Tokyo", "New York", "Florida", "China", "Delaware"]

print("list of places:")
print(Places)

print("\n list of places: (organized)")
print(sorted(Places))

print("\n Original List")
print(Places)

print("\n list of places: (reverse organized)")
print(sorted(Places, reverse=True))

print("\n Original List")
print(Places)

print("\n list of places: (reversed)")
Places.reverse()
print(Places)

print("\n list of places: (reversed again)")
Places.reverse()
print(Places)

Places.sort()
print("\n list of places:(Sorted)")
print(Places)

Places.sort(reverse=True)
print("\n list of places: (sorted reverse)")
print(Places)