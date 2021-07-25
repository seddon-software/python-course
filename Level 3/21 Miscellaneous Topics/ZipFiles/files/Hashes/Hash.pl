##########################################################
#
#	hashes
#
##########################################################


# create a hash
my %salary;

$salary{"steve"}  = "25000";
$salary{"mary"}   = "31000";
$salary{"bill"}   = "999999999";
$salary{"kalif"}  = "23500";
$salary{"ash"}    = "52000";
$salary{"bill"}   = "888888888";

print %salary, "\n";

# print out keys and values
print keys   %salary, "\n";
print values %salary, "\n";

print $salary{"mary"}, "\n";
1
