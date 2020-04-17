#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) : This would be considered O(n) because it loops based on n, there are n number of operations


b) O (n^2) : This would be considered O (n^2) because of the nested loops, the while loop and the foo loop are both O(n).


c) O(n) : This would be considered O (n) due to the recursive call in which it calls itself n number of times only.

## Exercise II

Assume unlimited # of eggs (list) egg == i
if eggs get thrown from floor > f == egg is broken
if eggs get thrown from floor < f == egg is safe
Find the midpoint of the building
Consider midpoint to be f
At midpoint drop an egg
if egg breaks find new midpoint 
repeat process until eggs no longer break
Once eggs are safe, assume that floor and any floors underneath are safe
runtime complexity = O (log n)


