pokemon([X,Y],result(A,S)):- \+pokemon([X,Y],S);
							 \+loc([X,Y],result(A,S)).


time(T,result(A,S)):-(A=forward,
						time(T-1,S),
						loc([X,Y],D,S),
						loctowards([X,Y],D,[W,Z]),
						loc([W,Z],D,result(A,S)));
					  (time(T,S),
					  (\+A= forward;
					    (\+A = forward;
					   	 (\+loc([X,Y],D,S);
					   	  wall([X,Y],D))))).

loc([X,Y],D,result(A,S)):- (A = forward,
							loctowards([X,Y],D,[W,Z]),
							loc([W,Z],D,S),
							\+wall([W,Z],D));
						   
						   (A= left,
						   	goright(D,F),
							loc([X,Y],F,S));
							(A= right ,
							 goleft(D,F),
							 loc([X,Y],F,S));
							
							(loc([X,Y],D,S),
							(\+ A= forward;
							wall([X,Y],D));

							(\+ A=forward,
							 \+ A=left,
							 \+ A= right)).