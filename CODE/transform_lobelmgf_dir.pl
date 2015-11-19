#!/usr/local/bin/perl

use strict;

my $error=0;
my $dir="";
if ($ARGV[0]=~/\w/) { $dir="$ARGV[0]";} else { $dir="."; }

if ($error==0)
{
	if (opendir(dir,"$dir"))
	{
		my @allfiles=readdir dir;
		closedir dir;
		foreach my $filename (@allfiles)
		{
			if ($filename=~/\.mgf$/i)
			{
				print qq!$filename\n!;
				system(qq!perl transform_lobelmgf.pl "$dir/$filename"!);
			}
		}
	}
}

