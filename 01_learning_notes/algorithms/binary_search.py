# 输入：一个有序数组 pages = list(range(1, 1001))（共1000页）;目标页码 target = 389
# 输出：最后返回目标页码的索引（如果找到）或 -1（如果没找到）
pages = list(range(1, 1001))
target = 389
pages_search = []
low = 0
high = len(pages) - 1
while low <= high:
    mid = (low + high) // 2
    pages_search.append(pages[mid])
    if pages[mid] == target:
        break
    elif pages[mid] < target:
        low = mid + 1
    elif pages[mid] > target:
        high = mid - 1
print(mid)