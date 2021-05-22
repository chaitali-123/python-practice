if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks=student_marks[query_name]
    total=0
    for mark in query_marks:
        total=total+mark;
        avg=total/3
    format_float = "{:.2f}".format(avg)
    print(format_float)
    
    """
    Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50

"""
