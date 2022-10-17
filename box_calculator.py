box_five = (number_items // 5)
box_three = (number_items % 5) // 3
box_one = (number_items % 5) % 3
total = box_one + box_three + box_five
print(f'Big boxes used: {box_five}\n'
      f'Medium boxes used: {box_three}\n'
      f'Small boxes used: {box_one}\n'
      f'Total number of boxes used: {total}')

# Test Case 1
# Please enter specific number of items for storage: 38
# Big boxes used: 7
# Medium boxes used: 1
# Small boxes used: 0
# Total number of boxes used: 8

# Test Case 2
# Please enter specific number of items for storage: 9
# Big boxes used: 1
# Medium boxes used: 1
# Small boxes used: 1
# Total number of boxes used: 3
