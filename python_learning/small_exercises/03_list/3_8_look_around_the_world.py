# 想出至少 5 个你想去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
dream_destination = ["shanghai","new york","singapore","lhasa","ili"]
# 按原始排列顺序打印该列表。不要考虑输出是否整洁，只管打印原始 Python列表就好。
print(dream_destination)
# 使用 sorted() 按字母顺序打印这个列表，不要修改它。
print(sorted(dream_destination))
# 再次打印该列表，核实排列顺序未变。
print(dream_destination)
# 使用 sorted() 按与字母顺序相反的顺序打印这个列表，不要修改它。
print(sorted(dream_destination,reverse=True))
# 再次打印该列表，核实排列顺序未变。
print(dream_destination)
# 使用 reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
dream_destination.reverse()
print(dream_destination)
# 使用 reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
dream_destination.reverse()
print(dream_destination)
# 使用 sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
dream_destination.sort()
print(dream_destination)
# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
dream_destination.sort(reverse=True)
print(dream_destination)
