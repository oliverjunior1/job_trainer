def fun(**kwargs):
    for k, val in kwargs.items():
        print('%s == %s' % (k, val))


# Driver code
fun(s1 = 'Geeks', s2 = 'For', s3='Geeks')