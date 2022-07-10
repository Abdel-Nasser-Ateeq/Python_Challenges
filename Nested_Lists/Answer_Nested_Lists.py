if __name__ == '__main__':
    names= []
    scores=[]
    for _ in range(int(input())):
        name = input()
        names.append(name)
        score = float(input())
        scores.append(score)

    # Implement the nested list names_scores
    names_scores=[[names[i],scores[i]] for i in range(len(names))]

    # Sort elements in nested list based on score (val)
    names_scores.sort(key = lambda x: x[1])

    # print("After Sorting based on val (grade):")
    # print(names_scores)
    
    # Get all scores
    # NOTE: I've already had the grades -via the 'scores' list-
    # but I delebrately extrat them like this to learn how to deal with Nested Lists!!

    all_scores=[i[1] for i in names_scores]

    # print(type(all_scores))
    
    # Get unique scores
    lista2=[]
    def unique_ (lista):
        for ele in lista:
            if ele not in lista2:
                lista2.append(ele)
        return lista2

    unique_scores=unique_(all_scores)

    # print("Unique values")
    # print(unique_scores)

    # Get the second element --> (2nd least score)
    second=unique_scores[1]

    # print("second_least_score= "+str(second))

    # Save all (key,value) pairs that their values equle second_least_score
    output=[i for i in names_scores if i[1]==second]

    # Sort based on the name (key)
    output.sort(key = lambda x: x[0])

    # print("After sorting based on key (name):"+str(output))

    for i in output:
        print(i[0])
