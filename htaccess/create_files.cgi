#!/usr/local/bin/perl
# create_files.cgi
# Create an empty <Files> clause in a .htaccess file

require './htaccess-lib.pl';
&ReadParse();
$lref = &read_file_lines($in{'file'});
if ($in{'regexp'}) {
	if ($httpd_modules{'core'} >= 1.3) {
		$newdir = "<FilesMatch \"$in{'path'}\">";
		$enddir = "</FilesMatch>";
		}
	else {
		$newdir = "<Files ~ \"$in{'path'}\">";
		$enddir = "</Files>";
		}
	}
else {
	$newdir = "<Files \"$in{'path'}\">";
	$enddir = "</Files>";
	}
push(@$lref, $newdir);
push(@$lref, $enddir);
&flush_file_lines();
&redirect("htaccess_index.cgi?file=".&urlize($in{'file'}));

