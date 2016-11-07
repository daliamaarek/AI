:- initialization main.
totaltime(4, snode).
time(0, snode).
wall([0, 0], up).
wall([0, 0], left).
wall([0, 1], up).
wall([0, 1], right).
wall([0, 2], up).
wall([0, 2], left).
wall([0, 3], up).
wall([0, 3], down).
wall([0, 3], right).
wall([1, 0], left).
wall([1, 0], right).
wall([1, 1], left).
wall([1, 1], right).
wall([1, 2], left).
wall([1, 3], up).
wall([1, 3], down).
wall([1, 3], right).
wall([2, 0], down).
wall([2, 0], left).
wall([2, 0], right).
wall([2, 1], left).
wall([2, 2], down).
wall([2, 3], up).
wall([2, 3], down).
wall([2, 3], right).
wall([3, 0], up).
wall([3, 0], down).
wall([3, 0], left).
wall([3, 1], down).
wall([3, 2], up).
wall([3, 2], down).
wall([3, 3], up).
wall([3, 3], down).
wall([3, 3], right).
pokemon([0, 0], snode).
pokemon([1, 3], snode).
pokemon([2, 0], snode).
pokemon([3, 0], snode).
end([0, 0]).
loc([1, 1], left, snode, _).
direction(up).
direction(down).
direction(left).
direction(right).

pair([X,Y], R , C):-
(
	XX is R - 1,
	YY is C - 1,
	between(0,XX,X),
	between(0,YY, Y)
).

loctowards([X,Y], up, [W,Z]):-    (X is W + 1, Y is Z).
loctowards([X,Y], left, [W,Z]):-  (X is W,     Y is Z + 1).
loctowards([X,Y], right, [W,Z]):- (X is W,     Y is Z - 1).
loctowards([X,Y], down, [W,Z]):-  (X is W - 1, Y is Z).

locto([X,Y], up,   [W,Z]):-    (W is X - 1, Z is Y).
locto([X,Y], left, [W,Z]):-    (W is X,     Z is Y - 1).
locto([X,Y], right,[W,Z]):-    (W is X,     Z is Y + 1).
locto([X,Y], down, [W,Z]):-    (W is X + 1, Z is Y).

goright(D, Ddash):- 
				 (D = up,    Ddash  = right);
				 (D = right, Ddash  = down);
				 (D = down,  Ddash  = left);
				 (D = left,  Ddash  = up).

goleft(D, Ddash):- 
				(D = right, Ddash = up);
				(D = down,  Ddash = right);
				(D = left,  Ddash = down);
				(D = up,    Ddash = left).


in([X,Y], Rows, Columns):- X < Rows, Y < Columns , X > -1, Y > -1.

pokemon([X,Y],result(A,S)):- 
							 (
							 	pokemon([X,Y],S),
							 	poss(A,S),
							 	\+loc([X,Y],D, result(A,S), 500)
							 ).

poss(forward,S):-
		 (
		   pair([X,Y],2,2),
		   loc([X,Y],D,S,500),
		   \+wall([X,Y],D)
		 ).

poss(left,  _).
poss(right, _).

time(T,result(A,S)):-(  
                       A=forward,
                       TT is T - 1,
					   time(TT,S),
					   pair([X,Y],2,2),
					   loc([X,Y],D,S,500),
						   \+ wall([X,Y], D),
					   locto([X,Y],D,[W,Z]),
					   loc([W,Z],D,result(A,S),500)
					  );
					  (
					  time(T,S),
					  ( 
					  	poss(A,S),
					    \+ A = forward
					  )).

loc([X,Y],D,result(forward,S), Depth):-
						  ( 
						  	Depth > 0,
						    direction(D),
							loctowards([W,Z],D,[X,Y]),
							\+wall([W,Z],D),
							in([W,Z],2,2),
							Nd is Depth - 1,
							loc([W,Z],D,S, Nd)
						  ).
loc([X,Y],D,result(left,S), Depth):-
						   (
						   	Depth >0,
						   	direction(D),
						   	goright(D,F),
							Nd is Depth - 1,
							loc([X,Y],F,S, Nd)).
loc([X,Y],D,result(right,S), Depth):-
							(
							 Depth >0,
							 direction(D),
							 goleft(D,F),
							 Nd is Depth - 1,
							 loc([X,Y],F,S, Nd)
							 ).
loc([X,Y],D,result(A,S), Depth):-							
							(
							Depth > 0,
							Nd is Depth - 1,
							loc([X,Y],D,S, Nd),
							(
							  A = forward,
							  direction(D),
							  wall([X,Y],D)
							)
							, in([X,Y],2,2)
							).

pokemon(S):-
	(
	  pair([W,Z],2,2),
	  pokemon([W,Z],S)
	).

getTime(T):-
	between(0,1000,T).

iterativeDeepening(S,Depth):-
	query(S,Depth).

iterativeDeepening(S,Depth):-
	\+query(S,Depth),
	DD is Depth + 1,
	iterativeDeepening(S, DD).

query(S, Depth):-
	(
	  end([X,Y]),
	  loc([X,Y], D, S, Depth),
	  \+pokemon(S),
	  getTime(T),
	  time(T, S), 
	  totaltime(TT, snode),
	  T >= TT
	 ).

main :- 
    bagof(X, iterativeDeepening(X,1), L),
    write('\n'),
    write('\n'),
    write('Possible Solution:\n'),
    write(L),
    write('\n'),
    write('\n'),
    halt.