#!/usr/local/bin/perl

use strict;

my $dir=$ARGV[0];
my $line="";
# my %hash_scans = ();
print "Hi there\n";
my %hash = ();

print $dir;
if (opendir(dir,"$dir"))
{
	my @allfiles=readdir dir;
	foreach my $filename (@allfiles)
	{

		if($filename=~/\.mgf$/){
			print "$filename\n";
			if (open(IN, "$dir/$filename"))
			{
				print "$filename openned\n";
				my %hash = ();
				while($line=<IN>)
				{
					if($line=~/SCANS=(.*)/)
					{
						if($hash{$1})
						{
							print "$1 ";
						}
						$hash{$1}="A";
					}
				}

			}
		}
	}
}

# if(open(IN, $filename))
# {
# 	while($line=<IN>)
# 	{
# 		if($line=~/SCANS=(.*)/)
# 		{
# 			# print "$1\n";
# 			if($hash_scans{$1})
# 			{
# 				print "Duplicate! $1";
# 			}
# 			else
# 			{
# 				$hash_scans{$1} = "QwEw";
# 			}
# 		}
# 		# print $line;
# 	}
# }
