def create_string(lst):
    st = ""
    for word in lst:
        st +=(word+" ")
    return st;

l = ["This", "is", "very", "fantastic"]
output = create_string(l)
print(output)