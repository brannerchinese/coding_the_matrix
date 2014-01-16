# version code 778a5ea1ddbc+
# Please fill out this stencil and submit using the provided submission script.





## 1: Problem 0.8.3Tuple Sum
def tuple_sum(A, B): 
	'''
	Input:
	  -A: a list of tuples
	  -B: a list of tuples
	Output:
	  -list of pairs (x,y) in which the first element of the
	  ith pair is the sum of the first element of the ith pair in
	  A and the first element of the ith pair in B
	Examples:
	>>> tumple_sum([(1,2), (10,20)],[(3,4), (30,40)])
	[(4,6), (40,60)]
	'''
	return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]



## 2: Problem 0.8.4Inverse Dictionary
def inv_dict(d): 
	'''
	Input:
	  -d: dictionary representing an invertible function f
	Output:
	  -dictionary representing the inverse of f, the returned dictionary's
	   keys are the values of d and its values are the keys of d
	Examples:
	>>> inv_dict({'thank you': 'merci', 'goodbye':  'au revoir'})
	{'merci':'thank you', 'au revoir':'goodbye'}]
	'''
	return {d[k]:k for k in d}



## 3: Problem 0.8.5Nested Comprehension
def row(p, n): 
	'''
	Input:
	  -p: a number
	  -n: a number
	Output:
	  - n-element list such that element i is p+i
	Examples:
	>>>row(10,4)
	[10, 11, 12, 13]
	'''
	return [p + i for i in range(n)]

comprehension_with_row = [row(i, 20) for i in range(15)]

comprehension_without_row = [[i + j for j in range(20)] for i in range(15)]



## 4: Problem 0.8.10Probability_1
Pr_f_is_even = 0.7
Pr_f_is_odd  = 1 - 0.7



## 5: Problem 0.8.11Probability_2
#Please give your solution as a fraction

Pr_g_is_1    = "4/10"
Pr_g_is_0or2 = "6/10"

