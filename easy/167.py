# coding=utf-8


"""Two Sum II - Input array is sorted."""

# 另一个小改进后的写法
# dic = {}
# for i, num in enumerate(numbers):
#     if target-num in dic:
#         return [dic[target-num]+1, i+1]
#     dic[num] = i


def _two_sum(numbers, target):
    ans = [1, len(numbers)]
    while ans[0] < ans[1]:
        sum = numbers[ans[0] - 1] + numbers[ans[1] - 1]
        if sum == target:
            return ans
        if sum < target:
            ans[0] += 1
        else:
            ans[1] -= 1

if __name__ == '__main__':
    print (_two_sum([2, 3, 3], 6))
