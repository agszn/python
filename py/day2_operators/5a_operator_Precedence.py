# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
# print((6 + 3) - (6 + 3))

'''
Operator	            Description	
()	                    Parentheses	
**	                    Exponentiation	
+x  -x  ~x	            Unary plus, unary minus, and bitwise NOT	
*  /  //  %	            Multiplication, division, floor division, and modulus	
+  -	                Addition and subtraction	
<<  >>	                Bitwise left and right shifts	
&	                    Bitwise AND	
^	                    Bitwise XOR	
|	                    Bitwise OR	
==  !=  >  >=  <  <=  
is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                    Logical NOT	
and	                    AND	
or	                    OR	

If two operators have the same precedence, the expression is evaluated from left to right.

'''
print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
