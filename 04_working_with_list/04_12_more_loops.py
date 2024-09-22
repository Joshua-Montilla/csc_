my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are;")
for m in my_foods:
    print(m)
print("\nMy friend's favorite foods are")
for f in friend_foods:
    print(f)
