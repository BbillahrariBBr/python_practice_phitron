actors = [
    {'name':'sakib khan', 'age':34},
    {'name':'kalman khan', 'age':54},
    {'name':'aharukh khan', 'age':52},
    {'name':'zolaiman khan', 'age':23},
    {'name':'bappi khan', 'age':29},
]

sorted_actor = sorted(actors, key= lambda actor: actor['name'], reverse=False)
print(sorted_actor)