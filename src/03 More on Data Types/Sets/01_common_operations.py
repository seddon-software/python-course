############################################################
#
#    sets
#
############################################################


myset = set(("Monday", "Tuesday"))
myset.add("Wednesday")
myset.add("Thursday")
myset.add("Friday")

print(myset)

if "Wednesday" in myset: print("member")
myset.remove("Wednesday")
if "Wednesday" not in myset: print("not a member")


1
