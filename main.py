
def read_assignment(line):
    parts = line.split(',')
    left = parts[0].split('-')
    right = parts[1].split('-')    
    return Assignment(int(left[0]), int(left[1]), int(right[0]), int(right[1]))

def left_inside_right(one_left, one_right, two_left, two_right):
    return one_left >= two_left and one_left <= two_right and one_right <= two_right and one_right >= two_left

class Assignment:
    def __init__(self, first_left, first_right, second_left, second_right):
        self.first_left = first_left
        self.first_right = first_right
        self.second_left = second_left
        self.second_right = second_right
    
    def inside(self):
        return left_inside_right(self.first_left, self.first_right, self.second_left, self.second_right) or \
        left_inside_right(self.second_left, self.second_right, self.first_left, self.first_right)

    def disjoint(self):
        return self.first_right < self.second_left or self.first_left > self.second_right

    def overlap(self):
        return not self.disjoint()

assignments = []
        
with open('Input.txt') as f:
    for line in f:
        assignments.append(read_assignment(line))

filtered = list(filter(lambda assignment: assignment.overlap(), assignments))

print(len(filtered))