# def fun(arg1, **kwargs):
#     for k, val in kwargs.items():
#         print('%s == %s' % (k, val))
#
#
# # Driver code
# fun('Hi', s1='Geeks', s2='for', s3='Geeks')


def family(**kwargs):
    for member, name in kwargs.items():
        print('%s =%s' % (member, name))


family(Father='Joaquim', Mather='Alyne', Daughter='Mariane', Son='Joao')