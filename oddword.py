def solution(num):
    if num % 2 == 0:
        return "a" * (num - 1) + "b"
    return "a" * num


print(solution(4))
print(solution(7))
print(solution(1))
print(solution(200000))
