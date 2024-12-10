# current O(nlogn), can optimise by heapifying + heappop to O(n)
def calculate_total_distance(list1, list2):
    l1_sorted = sorted(list1)
    l2_sorted = sorted(list2)

    distance = 0

    for i in range(len(l1_sorted)): 
        current_distance = abs(l2_sorted[i] - l1_sorted[i])
        distance += current_distance
    
    return distance


# current O(n) after optimisation
def calculate_simularity_score(list1, list2):
    score = 0
    l2_dict = {}

    for num in list2:
        if num not in l2_dict:
            l2_dict[num] = 1
        else:
            l2_dict[num] += 1

    for num in list1:
        if num in l2_dict:
            score += num * l2_dict[num]

    return score


input_file = "day1_input.txt"

list1 = []
list2 = []

with open(input_file) as file:
    for line in file:
        l1, l2 = line.split("   ")
        list1.append(int(l1.strip()))
        list2.append(int(l2.strip()))


print(f'total distance = {calculate_total_distance(list1, list2)}')

print(f'simularity score = {calculate_simularity_score(list1, list2)}')