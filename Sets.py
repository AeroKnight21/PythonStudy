cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Design', 'Art'}

print(cs_courses)

print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))
