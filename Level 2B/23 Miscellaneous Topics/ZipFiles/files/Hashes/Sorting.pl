##########################################################
#
#	sorting
#
##########################################################

use strict;
my %stdcode;
my ($PHONE, $line);

open ($PHONE, "<", "stdcode.uk") || die ("open failed");
while (my $line = <$PHONE>) {
	chop($line);
	my ($code, $town) = split(/\s+/,$line);
	$stdcode{$town} = $code;
}

my @towns = keys (%stdcode);

foreach my $town (sort @towns){
	printf ("%8s %s\n",$stdcode{$town},$town);
}

