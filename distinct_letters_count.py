import string


def solution(input_string):
    char_count = [input_string.count(char) for char in string.ascii_lowercase]
    # этот способ подсчета символов в ~1.5 раза быстрее, чем через collections.Counter
    # и в ~4 раза, чем через цикл и словарь/список

    deletions = 0
    max_freq = len(input_string)

    for freq in sorted(char_count, reverse=True):
        if freq > max_freq:
            deletions += freq - max_freq
            freq = max_freq

        max_freq = max(0, freq - 1)

    return deletions


print("aaaabbbb: ", solution("aaaabbbb"))
print("ccaaffddecee: ", solution("ccaaffddecee"))
print("eeee: ", solution("eeee"))
print("example: ", solution("example"))
