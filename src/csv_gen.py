from itertools import zip_longest

with open('../log.txt', 'r') as f:
    d={}
    # 1000,A:51,RND:49
    for line in f.readlines():
        _,n,b = line.split(',')
        n_id, n_val = n.split(':')
        b_id, b_val = b.split(':')

        # if b_id != 'MC_1000':
        if True:
            key = n_id + ' v ' + b_id
            if key not in d:
                d[key] = []

            d[key].append(n_val)

    print(','.join(['i'] + list(d.keys())))
    i=0
    for row in list(zip_longest(*[list(l) for l in d.values()], fillvalue='0')):
        print(','.join([str(i)] + list(row)))
        i += 1

