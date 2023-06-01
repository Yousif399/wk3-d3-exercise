#Exercise1
# words = ['this' , 'is', 'a', 'sentence', '.']

# def reverse(list_names,a,b,c,d,e):
#     list_names[a],list_names[b],list_names[c],list_names[d],list_names[e],=list_names[e],list_names[d],list_names[c],list_names[b],list_names[a]

# reverse(words,4,3,2,1,0)
# print(words)

#Exercise2
# a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
# b_text=" i am i am i am I AM"
# def count_words(names):
#     distinct_words={'i': 1}
#     names = names.split()
#     for name in names:
#         name = name.lower()
#         if name in distinct_words:
#             distinct_words[name] += 1
#         else:
#             distinct_words[name] = 1
#     return distinct_words
# print(count_words(a_text))
# print(count_words(b_text))


#Exercise3
# def lin_search(list,y,x):
#     for i in range(0,y):
#         if list[i] == x:
#             return f"answer found at index: {i}"
        
#     return 'answer is not founded'
# list =[1,4,78,55,89,9,90,3]
# x=55
# y=len(list)
# answer= lin_search(list,y,x)
# print(answer)

#Exercise3-using binary search
def lin_search2(list,x):

    left_side = 0
    right_side = len(list)-1

    while left_side <= right_side:
        mid = (left_side + right_side) // 2
        if list[mid] == x:
            return f" answer founded at index: {mid}"
            
        elif list[mid] < x:
            left_side = mid +1
        else:
            right_side = mid -1
    return False
                
list =[1,4,78,55,89,9,90,3,10008,9994,484,884,34,10500]
x=10500
answer2= lin_search2(list,x)
print(answer2)

