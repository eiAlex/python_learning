import collections

grades = [83, 95 ,91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade / 10 * 10
histogram = collections.Counter(decile(grade) for grade in grades)
