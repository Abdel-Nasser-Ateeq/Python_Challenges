if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n in range(2,11):
        for _ in range(n):
            # *line --> all elements after the 1st one
            #  will be stored in var 'line' as a list
            name, *line = input().split()
            
            # map(func, input) receive two input a function
            # and an input to that function
            scores = list(map(float, line))
            
            student_marks[name] = scores
        query_name = input()

# print(student_marks)

def check(lista):
    output= False
    if len(lista)==3:
        for _ in lista:
            if _ in range(0,101):
                output=True
    return output
                
result= check(scores) 
if result:
    SUM=0
    value = student_marks[str(query_name)]
    for i in value:
        SUM= SUM+i
    out =str(SUM/len(value))
    num = out.split('.')
    if len(num[1])==1:
        num[1] = num[1]+'0'
    print(num[0]+'.'+num[1][:2])
# https://www.hackerrank.com/challenges/finding-the-percentage
