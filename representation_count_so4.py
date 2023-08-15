import itertools

# Count the number of "good" so(4)-representations of
# \pi_1^{orb}(T^8/\Gamma) -- uniquely determined by their values on
# \gamma, \delta, \tau_4, \tau_5, \tau_8 -- into
# \{1,a,b,c,-1,-a,-b,-c\}, (denoted in the code as \{1,2,3,4,-1,-2,-3,-4\}).
# Representations are denoted as 5-tuples of group elements, e.g.
# (1,1,3,2,1) denotes the representation
# \rho(\gamma)=\rho(\delta)=\rho(\tau_8)=1, \rho(\tau_4)=b, \rho(\tau_5)=a.
# By "good" representations we mean those that can be used
# in our Spin(7)-instanton construction, i.e. satisfies the following two conditions:
# (i) at least one of \rho(\gamma), \rho(\delta) is not the identity
# (ii) at least two of the values \{a,b,c\} or at least two of the values
# \{-a,-b,-c\} appear among
# \{ \rho(\tau_4), \rho(\tau_5), \rho(\tau_8) \}.

all_solutions = []
repvalues = [1,2,3,4,-1,-2,-3,-4]
for rep in itertools.product(repvalues,repvalues,repvalues,repvalues,repvalues):
    if (2 in rep[2:] and 3 in rep[2:]) or \
            (2 in rep[2:] and 4 in rep[2:]) or \
            (3 in rep[2:] and 4 in rep[2:]) or \
            (-2 in rep[2:] and -3 in rep[2:]) or \
            (-2 in rep[2:] and -4 in rep[2:]) or \
            (-3 in rep[2:] and -4 in rep[2:]):
        if not (rep[0]==1 and rep[1]==1):
            all_solutions += [list(rep)]

print('List of all good representations:')
print(all_solutions,len(all_solutions))
print('To obtain the notation from the paper, substitute 1->Id, 2->a, 3->b, 4->c')

# gauge transformations that are extensions from so3
gauge1 = { 1: 1, 2: 3, 3: 4, 4: 2,
          -1:-1,-2:-3,-3:-4,-4:-2}
gauge2 = { 1: 1, 2: 3, 3: 2, 4: 4,
          -1:-1,-2:-3,-3:-2,-4:-4}
gauge3 = { 1: 1, 2: 2, 3: 4, 4: 3,
          -1:-1,-2:-2,-3:-4,-4:-3}
gauge4 = { 1: 1, 2: 4, 3: 2, 4: 4,
          -1:-1,-2:-4,-3:-2,-4:-4}
gauge5 = { 1: 1, 2: 4, 3: 3, 4: 2,
          -1:-1,-2:-4,-3:-3,-4:-2}
so3gauges = [gauge1,gauge2,gauge3,gauge4,gauge5]
# new in so4
gauge6 = { 1: 1, 2:-2, 3:-3, 4: 4,
          -1:-1,-2: 2,-3: 3,-4:-4}
gauge7 = { 1: 1, 2:-2, 3: 3, 4:-4,
          -1:-1,-2: 2,-3:-3,-4: 4}
gauge8 = { 1: 1, 2: 2, 3:-3, 4:-4,
          -1:-1,-2:-2,-3: 3,-4: 4}
so4gauges = [gauge6,gauge7,gauge8]

def comp(gaugeA, gaugeB):
    gaugeComp = {}
    for key in gaugeA:
        gaugeComp[key] = gaugeB[gaugeA[key]]
    return gaugeComp


# Now quotienting out by gauge transformations
def gauge_transform(rep):
    gauge_comps = [
        comp(gaugeA, gaugeB) for gaugeA in so3gauges for gaugeB in so4gauges
    ]
    all_gauges = gauge_comps + so3gauges + so4gauges

    return [
        [gauge[letter] for letter in rep] for gauge in all_gauges
    ]

while True:
    total_removed = 0
    for rep in all_solutions:
        removed_during_this_iteration = 0
        # need to distinguish between total_removed and
        # removed_during_this_iteration, because while the for loop
        # is executed, list elements are deleted, which may lead to list
        # elements not being checked
        for gauged_rep in gauge_transform(rep):
            try:
                all_solutions.remove(gauged_rep)
                removed_during_this_iteration += 1
                total_removed += 1
                print(f'removed {gauged_rep}. Total removed: {total_removed}. Total remaining: {len(all_solutions)}')
            except ValueError as e:
                pass
        # print(f'# removed: %s', (removed_during_this_iteration))
    if total_removed == 0:
        break

print(all_solutions)
print(len(all_solutions))