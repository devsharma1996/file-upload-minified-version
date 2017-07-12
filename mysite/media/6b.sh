echo "enter the string:"
read string
len=${#string}
revstr=""
while ([ $len -gt 0 ])
do
	revstr=$revstr$(echo $string|cut -c $len)
	let len-=1
done
echo $revstr
