import itertools

# Count the number of "good" representations of
# \pi_1^{orb}(T^8/\Gamma) -- uniquely determined by their values on
# \gamma, \delta, \tau_1, \tau_4, \tau_8 -- into the Klein
# four group \{1,a,b,c\}, (denoted in the code as \{1,2,3,4\}).
# Representations are denoted as 5-tuples of group elements, e.g.
# (1,1,3,2,1) denotes the representation
# \rho(\gamma)=\rho(\delta)=\rho(\tau_8)=1, \rho(\tau_1)=b, \rho(\tau_4)=a.
# By "good" representations we mean those that can be used
# in our Spin(7)-instanton construction, i.e. satisfies the following two conditions:
# (i) at least one of \rho(\gamma), \rho(\delta) is not the identity
# (ii) at least two of the values \{a,b,c\} appear among
# \{ \rho(\tau_1), \rho(\tau_4), \rho(\tau_8) \}.

# Counting "good" representations
all_reps = []
reps_which_start_with_one_one = []
reps_with_one_a_in_last_three_places = []
reps_with_one_b_in_last_three_places = []
reps_with_one_c_in_last_three_places = []
multiple_counted_bad_ones = 0

repvalues = [1,2,3,4]
for rep in itertools.product(repvalues,repvalues,repvalues,repvalues,repvalues):
    bad_properties = 0
    all_reps += [all_reps]
    if rep[0] == 1 and rep[1] == 1:
        reps_which_start_with_one_one += [rep]
        bad_properties += 1
    if rep[2] in [1,2] and rep[3] in [1,2] and rep[4] in [1,2]:
        reps_with_one_a_in_last_three_places += [rep]
        bad_properties += 1
    if rep[2] in [1,3] and rep[3] in [1,3] and rep[4] in [1,3]:
        reps_with_one_b_in_last_three_places += [rep]
        bad_properties += 1
    if rep[2] in [1,4] and rep[3] in [1,4] and rep[4] in [1,4]:
        reps_with_one_c_in_last_three_places += [rep]
        bad_properties += 1
    if bad_properties > 0:
        multiple_counted_bad_ones += bad_properties-1

print('Number of good representations:')
print(len(all_reps)-len(reps_which_start_with_one_one)-len(reps_with_one_a_in_last_three_places)-len(reps_with_one_b_in_last_three_places)-len(reps_with_one_c_in_last_three_places)+multiple_counted_bad_ones)


# Explicitly construction all solutions
# First without quotienting out by gauge transformations
all_solutions = []
repvalues = [1,2,3,4]
for rep in itertools.product(repvalues,repvalues,repvalues,repvalues,repvalues):
    if (2 in rep[2:] and 3 in rep[2:]) or (2 in rep[2:] and 4 in rep[2:]) or (3 in rep[2:] and 4 in rep[2:]):
        if not (rep[0]==1 and rep[1]==1):
            all_solutions += [list(rep)]

print('List of all good representations:')
print(all_solutions,len(all_solutions))
print('To obtain the notation from the paper, substitute 1->Id, 2->a, 3->b, 4->c')


# Now quotienting out by gauge transformations
def gauge_transform(rep):
    def gauge1(letter):
        if letter==1:
            return 1
        if letter==2:
            return 3
        if letter==3:
            return 4
        if letter==4:
            return 2
    def gauge2(letter):
        if letter==1:
            return 1
        if letter==2:
            return 3
        if letter==3:
            return 2
        if letter==4:
            return 4
    def gauge3(letter):
        if letter==1:
            return 1
        if letter==2:
            return 2
        if letter==3:
            return 4
        if letter==4:
            return 3
    def gauge4(letter):
        if letter==1:
            return 1
        if letter==2:
            return 4
        if letter==3:
            return 2
        if letter==4:
            return 4
    def gauge5(letter):
        if letter==1:
            return 1
        if letter==2:
            return 4
        if letter==3:
            return 3
        if letter==4:
            return 2
    return [
        [gauge1(letter) for letter in rep],
        [gauge2(letter) for letter in rep],
        [gauge3(letter) for letter in rep],
        [gauge4(letter) for letter in rep],
        [gauge5(letter) for letter in rep],
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
            except ValueError as e:
                pass
        # print(f'# removed: %s', (removed_during_this_iteration))
    if total_removed == 0:
        break

print(all_solutions)
print(len(all_solutions))
