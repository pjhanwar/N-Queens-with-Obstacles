# N-Queens-with-Obstacles

The code is an implementation of traditional n-queens problem with obstacles using 3 algorithms:<br>
Depth First Search<br>
Breadth First Search &<br>
Simiulated Annealing<br>

If an obstacle is present in a row of the borad, the queen can be placed at either side of the obstacle without attacking each other.

# Input: 
The	input	should	be	formatted	as	follows:<br>
First	line:	 instruction	of	which	algorithm	to	use:	BFS,	DFS	or	SA<br>
Second	line:	 strictly	positive	32-bit	integer	n,	the	width	and	height	of	the	square	board<br>
Third	line:	 strictly	positive	32-bit	integer p,	the	number	of	queens<br>
Next	n	lines:	 the	n	x	n	board,	one	file	line	per	board	row	<br>
It	will	have	a	0	where	there	is	nothing,	and	a	2	where	there	is	an obstacle.<br>

# Output:	
The	file	output.txt is	formatted	as	follows:<br>
First	line:	 OK or FAIL, indicating	whether	a	solution	was	found	or	not.<br>
Next	n	lines:	 the	n	x	n	board,	one	line in	the	file per	nursery	row,	including	the	queens and	obstacles. 
It	will	have	a	0	where	there	is	nothing,	a	1	where	you	placed	a	queen, and a	2	where	there	is	an obstacle.	

### Example	1:
For	this	input.txt:<br>
BFS<br>
2<br>
2<br>
00<br>
00<br>

one	possible	correct	output.txt	is:<br>
FAIL<br>

### Example	2:
For	this	input.txt:<br>
DFS<br>
4<br>
4<br>
0000<br>
0000<br>
0000<br>
0000<br>

one	possible	correct	output.txt	is:<br>
OK<br>
0010<br>
1000<br>
0001<br>
0100<br>

### Example	3:
For	this	input.txt:<br>
SA<br>
8<br>
9<br>
00000000<br>
00000000<br>
00000000<br>
00002000<br>
00000000<br>
00000200<br>
00000000<br>
00000000<br>

one	possible	correct	output.txt	is:<br>
OK<br>
00000100<br>
10000000<br>
00001000<br>
01002001<br>
00001000<br>
00100200<br>
00000010<br>
00010000<br>
