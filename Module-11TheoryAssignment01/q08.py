
numbers= [10,20,10,40,50,60,70]
target=50
default_number = 0
default_position = 0
for i, num in enumerate(numbers):
    if num+default_number != target:
        default_number = num
        default_position = i
    elif num+default_number == target:
        print(f'{default_position+1}, {i+1}')