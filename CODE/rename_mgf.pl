#!c:/perl/bin/perl.exe
#

use strict;

my $error=0;
my $dir=0;
if ($ARGV[0]=~/\w/) { $dir=$ARGV[0];} else { $error=1; }

if ($error==0)
{
	if (opendir(dir,"$dir"))
	{
		my @allfiles=readdir dir;
		closedir dir;
		foreach my $filename (@allfiles)
		{
			if ($filename=~s/\.mgf\.mgf$/\.mgf/i)
			{
				system(qq!mv $dir/$filename.mgf $dir/$filename!);
			}
		}
	}
}