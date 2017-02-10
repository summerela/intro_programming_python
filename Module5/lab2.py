import sys

def increment_counter(str1, counter):
    for s in str1:
        counter[s] = counter.get(s, 0) + 1
    return counter

def is_anagram(str1, str2):
    # do QC here
    str1, str2 = str1.lower(), str2.lower()

    counter1 = increment_counter(str1, {})
    counter2 = increment_counter(str2, {})
    return counter1 == counter2

print(is_anagram(sys.argv[1], sys.argv[2]))

