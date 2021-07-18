
#
# Output the Captain's room number.
#

import collections

n = int(input())
k = list(map(int,input().split(' ')))

mc = collections.Counter(k).most_common()

print(mc[-1][0])