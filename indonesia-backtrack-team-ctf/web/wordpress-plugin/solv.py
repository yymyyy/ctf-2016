<?php
// Author: @yansen1204

$email = "ctf-ibt@mail.com";
$email = strtoupper($email);
$email = str_split($email);
$active = array();
$cnt = array();
$max = 0;
for($i=0;$i<count($email);$i++)
{
	for($j=1;$j<256;$j++)
	{
		if(( $j%2 ? $j/3 : $j/2  ) == ord($email[$i]) ){
			array_push($cnt, $j);
		}
	}
	$max = max($cnt);
	array_push($active, $max);
	$cnt = array();
}

$act = serialize($active);
$x = base64_encode(gzcompress($act));
echo $x;

// IBT2016{eJxFTtsRgDAIWwlKqYLT+NkZvO4uyXn1g1wKefROHfnMlGtmEy3kjBNvsI6LgZkXduw1Cp07aMZ2HGANjH5DFrQaVMs2K1ucDYAgs/8T7DHm+Re1XuLoK7w=}
?> 
