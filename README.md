# Wordle-Solver

Simple Python program to solve Wordles

Solved by  
1. Finding an initial word from words.txt, that has a combination of the most frequently used letters. In this case - "arose".
2. Asking for the result: "n" - Grey/Not a letter, "y" - Yellow/A letter in the wrong position, "g" - Green/A letter in the correct position
3. Sieving out remaining possible words

Added function:
Scenarios might arise such that an input, e.g. "Patch" - may return the result "ngggg".  
In such case, possible words may include: Batch, Catch, Hatch, Watch, etc. Too many attempts would be wasted trying to solve the Wordle.  
Hence, the program recognises these scenarios, examines the possible words, and finds a word with the combination of the remaining letter.  
E.g. The best combination of "B", "C", "H", and "W" is "which". It will be used to test for the remaining letter
