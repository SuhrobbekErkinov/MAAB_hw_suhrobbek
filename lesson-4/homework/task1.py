def uncommon_elements(list1, list2):
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    uncommon = []
    for key in count1.keys() & count2.keys():
        diff = count1[key] - count2[key]
        if diff != 0:
            uncommon.extend([key] * abs(diff))

    for key in count1.keys() ^ count2.keys():
        uncommon.extend([key] * (count1[key] or count2[key]))

    return uncommon

def test1():
    list1 = [1, 1, 1, 2, 3, 4]
    list2 = [1, 1, 2, 2, 3, 3, 5, 4]
    print(uncommon_elements(list1, list2))

if __name__ == '__main__':
    test1()