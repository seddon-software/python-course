##########################################################
#
#        Undefined
#
##########################################################


#            Key(Name) => Values(Phone)


%PhoneBook = ("John"   => "7145",
              "Mary"   => "3110",
              "Steven" => "4669",
              "Angela" => "2201",
              "Bjorn"  => "5989");


# undefine an entry
$PhoneBook{'Steven'} = undef;

# check if each entry is defined
foreach $entry (keys %PhoneBook) {
    if(defined $PhoneBook{$entry}) {
        print "$entry defined \n";
    } else {
        print "$entry NOT defined \n";
    }
}
print "---------------\n";

# delete an entry
delete $PhoneBook{'Mary'};

# check if each entry exists
foreach $entry qw(John Mary Steven Angela Bjorn) {
    if(exists $PhoneBook{$entry}) {
        print "$entry exists \n";
    } else {
        print "$entry does NOT exist \n";
    }
}



