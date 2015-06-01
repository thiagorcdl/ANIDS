__author__ = 'thiago'

import sys


def search(n, item_list, instances, files, tholds):
    f = open(files[n], "r")
    if n == 1:
        for line in f:
            split = line.split()
            if len(split) == 4 and int(split[0]) <= instances:
                if int(split[3]) < tholds[n]:
                    # Adds to rejection list
                    item_list.extend(int(split[3]))
                else:
                    # Prints as valid output
                    print line
    else:
        for line in f:
            split = line.split()
            if len(split) == 4 and int(split[0]) in item_list:
                if int(split[3]) >= tholds[n]:
                    # Prints as valid output
                    print line
                    # Removes from rejection list
                    item_list.remove(int(split[3]))
    return item_list


if __name__ == "__main__":
    instances = 0
    argc = len(sys.argv)
    if argc < 2:
        print "Usage:\n\t%s <file1> <threshold1> ... <fileN> <thresholdN>" % sys.argv[0]
    num_classifiers = (argc - 1) / 2
    rejected = []
    files = [" "] + [sys.argv[x] for x in range(1, num_classifiers + 1, 2)]
    tholds = [0] + [int(sys.argv[x]) for x in range(2, num_classifiers + 1, 2)]

    # Retrieves total number of instances
    f = open(files[1], "r")
    for line in f:
        split = line.split()
        if len(split) == 2 and split[0] == "Instances:":
            instances = int(split[1])
            break

    # Iterates through files
    for i in xrange(1, num_classifiers + 1):
        rejected = search(i, rejected, instances, files, tholds)
    print "Rejected items:"
    print rejected
    sys.exit(0)