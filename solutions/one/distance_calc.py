# Load Lists + Sort
file = open("input.txt", "r")

list_one = []
list_two = []

distance = 0

for line in file:
    ids = line.split()
    list_one.append(int(ids[0]))
    list_two.append(int(ids[1]))

file.close()

list_one.sort()
list_two.sort()

frequency_table = {}

for first_location, second_location in zip(list_one, list_two):
    # Calculate Distance (Part One)
    distance += abs(first_location - second_location)
    # Populate Frequency Table (Part Two)
    frequency_table[second_location] = frequency_table.get(second_location, 0) + 1

print(distance)


# Calculate Similarity Score (Part Two)
similarity_score = 0

for location in list_one:
    similarity_score += frequency_table.get(location, 0) * location

print(similarity_score)

# Answer to Part One:
# 3246517

# Answer to Part Two:
# 29379307