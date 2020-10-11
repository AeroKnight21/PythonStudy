def student(name, age, *marks):
    print("name:", name)
    print('age:', age)
    print('marks:', marks)
    for x in marks:
        print(x)


student('Joel', 20, 90, 80, 100, 91)

# * is for list and ** is for keyword arguments
