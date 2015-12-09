Python script that generates a JS array of objects  from option tags within a select tag in an HTML file

Input: id of the select menu, name of output JS file

Output: JS file with containing an array of objects with format:

var {object_name} = [
	{abbr: "{abbr}", {id}: "{option_text}"}.
	...

]

Useful for selecting the value and inner text of all option tags in a select list