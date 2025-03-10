try:
    my_dict={'name':'Yogesh'}
    print(my_dict['age'])
except KeyError as e:
    print("There is an Error",e)