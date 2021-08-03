##########################################################
#
#        hash slices
#
##########################################################


# create a hash

$salary{"steve"}  = "25000";
$salary{"mary"}   = "31000";
$salary{"bill"}   = "999999999";
$salary{"kalif"}  = "23500";
$salary{"ash"}    = "52000";

# print out keys and values
($bill, $ash, $mary) = @salary{'bill', 'ash', 'mary'};
print "Bill: $bill \n";
print "Ash:  $ash  \n";
print "Mary: $mary \n";

1