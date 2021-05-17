##########################################################
#
#        towns
#
##########################################################

use strict;
my %stdcode;

open(my $PHONE, "<", "codes.txt") || die ("open failed");
while(my $line = <$PHONE>) {
  chop($line);
  my ($code,$town) = split(/\s+/,$line);
  $stdcode{$town} = $code;
}

print "Town: ";
chop (my $townToFind=<STDIN>);
if ($stdcode{$townToFind}) {
  print "The code for $townToFind is $stdcode{$townToFind}\n";
} else {
  print "$townToFind is not in the database\n";
}

1;

