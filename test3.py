courses = ['history', 'math', 'physics', 'geo']  # lists
courses2 = ['Art', 'Education']
print(len(courses))
print(courses[0:3])  # slicing
courses.append('Art')  # adding
# courses.insert(0, courses2)
# courses.extend( courses2)
courses.remove('math')
popped = courses.pop()
courses.reverse()
courses.sort()
print(courses)

for i in courses:
    print(i)

# Mutable list we acn used if we want to modify []

# Immutable tuples don't support modification ()

# sets : values unordered and have no duplicates {}
