if __name__ == '__main__':
    names= []
    scores=[]
    for _ in range(int(input())):
        name = input()
        names.append(name)
        score = float(input())
        scores.append(score)
    n_scores=[[names[i],scores[i]] for i in range(len(names))]
    n_scores.sort(key = lambda x: x[1])
    # print("After Sorting based on val (grade):")
    # print(n_scores)
    np_input=[i[1] for i in n_scores]
    # print(type(np_input))
    lista2=[]
    def unique_ (lista):
        for ele in lista:
            if ele not in lista2:
                lista2.append(ele)
        return lista2

    xx=unique_(np_input)
    # print("Unique values")
    # print(xx)
    second=xx[1]
    # print("second_least_grade= "+str(second))
    output=[i for i in n_scores if i[1]==second]
    output.sort(key = lambda x: x[0])
    # print("After sorting based on key (name):"+str(output))
    for i in output:
        print(i[0])
        # print(i[1])
# The challenge is available via this link:
# https://www.hackerrank.com/challenges/nested-list
