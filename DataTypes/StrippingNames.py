# Store a person’s name, and include some whitespace characters at the beginning and end of the name  Make sure you use each character combination, "\t" and "\n", at least once
# Print the name once, so the whitespace around the name is displayed  Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip()


name = "\t   Forrest  Gump        \n"


def printStrippedName(name):
    print(name)

    print(name.rstrip(" "))
    print(name.rstrip("\n"))

    print(name.lstrip("\t "))
    print(name.lstrip(" "))

    print(name.strip(" "))


printStrippedName(name)
