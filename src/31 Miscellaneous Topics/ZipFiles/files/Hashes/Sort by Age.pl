##########################################################
#
#        Sort by Age
#
##########################################################

%people = ('Mary'   => 34,
           'Steve'  => 17,
           'Ali'    => 61,
           'Peter'  => 27,
           'Lesley' => 49,
           'John'   => 18);

@peopleByAge = sort byAge keys %people;

foreach $person (@peopleByAge) {
    printf("%-10s%i\n", $person, $people{$person});
}

##########################################################

sub byAge {
    return  1 if($people{$a} <  $people{$b});
    return  0 if($people{$a} == $people{$b});
    return -1 if($people{$a} >  $people{$b});
}