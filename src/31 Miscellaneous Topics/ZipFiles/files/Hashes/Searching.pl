##########################################################
#
#	searching
#
##########################################################

use strict;
my %stdcode;
my ($PHONE, $line);

open ($PHONE, "<", "stdcode.uk") || die ("open failed");
while ($line = <$PHONE>) {
	chomp($line);
	my ($code,$town) = split(/\s+/,$line);
	$stdcode{$town} = $code;
}

my @towns = keys(%stdcode);
print "Town: ";
my $pattern = <STDIN>;
chop $pattern;
my @selected = grep(/$pattern/i,@towns);

foreach my $town (@selected){
	printf ("%8s %s\n",$stdcode{$town},$town);
}

1