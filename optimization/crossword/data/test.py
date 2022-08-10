#!/usr/bin/env python3


with open("structure0.txt") as f:
            contents = f.read().splitlines()
            #print(contents)
            height = len(contents)
            width = max(len(line) for line in contents)

            structure = []
            for i in range(height):
                row = []
                for j in range(width):
                    if j >= len(contents[i]):
                        row.append(False)
                    elif contents[i][j] == "_":
                        row.append(True)
                    else:
                        row.append(False)
                structure.append(row)

for i in range(height):
            for j in range(width):

                # Vertical words
                starts_word = (
                    structure[i][j]
                    and (i == 0 or not structure[i - 1][j])
                )


print(starts_word)


print(structure)