#filter_list.py

li = [ 1, "1", 55,"123", 123]

def filter_list(lis): 
    return [*filter(lambda x: not isinstance(x, str), lis)]

if __name__ == "__main__" : 
    print(li)
    listy = filter_list(li) 
    print(listy)
