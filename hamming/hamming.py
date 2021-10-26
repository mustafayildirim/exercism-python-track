def distance(strand_a, strand_b):

    if len(strand_a) == 0 and len(strand_b) == 0:
        return 0

    if len(strand_a) != len(strand_b):
        raise ValueError(".+")

    if not strand_a and strand_b:
        raise ValueError(".+")

    if not strand_b and strand_a:
        raise ValueError(".+")

    difference = 0
    for i, _ in enumerate(strand_a):
        if strand_a[i] == strand_b[i]:
            continue

        difference += 1

    return difference
