def all_partitions(sequence):

    if len(sequence) == 1:
        yield [sequence]
        return 
    first, *rest = sequence
    for smaller in all_partitions(rest):
        for n, subset in enumerate(smaller):
            yield smaller[ : n] + [[first] + subset] + smaller[n + 1 :]
        yield [[first]] + smaller