# Python Problem Solving — Master Reference

> **How to use this file:** Read the problem statement carefully. Understand the goal. Then read the approach and think through the steps before opening VSCode. Only start coding once you can explain the solution in plain English.

---

## Phase 1 — Variables & Data Types

> **Goal:** Understand how Python stores different kinds of data and how to perform basic input/output operations.

---

### P1.1 — Sum and Difference of Two Numbers
**Problem:** You are given two integers as input. Your task is to print four results — their sum, their difference, their product, and their quotient — each on a separate line.

**Approach:**
- Read two separate inputs using `input()` and convert them to integers using `int()`
- Store each result in a variable before printing
- Think about what happens if you divide two integers — does Python give you a float or an integer? Test both `//` (floor division) and `/` (true division)

**Tags:** HackerRank, Python Basics

---

### P1.2 — Area of a Rectangle
**Problem:** Given the length and width of a rectangle as input, calculate and print its area.

**Approach:**
- Read two numbers from input — decide whether they should be integers or floats
- Apply the formula: area = length × width
- Print the result with a clear label using an f-string

**Tags:** Python Basics

---

### P1.3 — Celsius to Fahrenheit Converter
**Problem:** Read a temperature value in Celsius and convert it to Fahrenheit. Print the result.

**Approach:**
- Read the input as a float since temperatures can be decimal values
- Apply the formula: F = (C × 9/5) + 32
- Think about operator precedence — multiplication happens before addition, so the formula works naturally
- Round the result to 2 decimal places for clean output

**Tags:** Python Basics, Key Concept

---

### P1.4 — Swap Two Variables Without a Third
**Problem:** Given two variables a and b, swap their values without using a temporary third variable. Print both values before and after the swap.

**Approach:**
- In most languages you need a temp variable: temp = a, a = b, b = temp
- Python allows tuple unpacking which lets you do this in one line
- Understand what tuple unpacking means — Python evaluates the right side completely before assigning to the left side
- This concept appears constantly in sorting algorithms later

**Tags:** Python Basics, Key Concept

---

### P1.5 — Check if a Number is Even or Odd
**Problem:** Read an integer and print whether it is Even or Odd.

**Approach:**
- Use the modulo operator `%` which gives you the remainder after division
- If a number divided by 2 has remainder 0, it is even — otherwise odd
- Think about edge cases: what happens with 0? What about negative numbers?

**Tags:** HackerRank, Python Basics

---

### P1.6 — Simple Interest Calculator
**Problem:** Read the principal amount, rate of interest, and time period. Calculate and print the simple interest.

**Approach:**
- Formula: SI = (P × R × T) / 100
- Decide the appropriate data types — principal and rate may be floats
- Print the result formatted to 2 decimal places
- This teaches you to map a real-world formula directly into code

**Tags:** Python Basics

---

### P1.7 — String Repetition and Concatenation
**Problem:** Read a string and a number n from input. Print the string repeated n times, and also print it concatenated with itself once.

**Approach:**
- Understand that in Python, `*` works on strings to repeat them
- Understand that `+` works on strings to join them
- These are the same operators as arithmetic but they behave differently on strings — this is called operator overloading
- Think about what happens if n is 0 or negative

**Tags:** HackerRank, Python Basics

---

### P1.8 — BMI Calculator
**Problem:** Read a person's weight in kilograms and height in metres. Calculate their BMI and print the corresponding category — Underweight, Normal, Overweight, or Obese.

**Approach:**
- Formula: BMI = weight / (height × height)
- First compute the BMI value
- Then use if-elif-else to classify it into the right category based on standard ranges
- This problem combines arithmetic with conditional logic — a preview of Phase 2

**Tags:** Python Basics, Key Concept

---

## Phase 2 — Operators

> **Goal:** Understand all Python operators — arithmetic, comparison, logical, and assignment — and how they form the decision-making backbone of your code.

---

### P2.1 — FizzBuzz
**Problem:** Print numbers from 1 to 100. But for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz".

**Approach:**
- The key insight is the order of your conditions — check for divisibility by both 3 and 5 first, before checking each individually
- If you check 3 first and 5 first separately, you will never reach the FizzBuzz case
- Use the modulo operator `%` to check divisibility
- This problem teaches you that the sequence of conditions matters enormously

**Tags:** HackerRank, LeetCode, Python Basics

---

### P2.2 — Find the Largest of Three Numbers
**Problem:** Read three numbers and print the largest one without using Python's built-in `max()` function.

**Approach:**
- Start by assuming the first number is the largest
- Compare it with the second — if the second is larger, update your assumption
- Compare your current largest with the third number — update again if needed
- This manual comparison logic is the foundation of sorting algorithms you will write later

**Tags:** HackerRank, Python Basics

---

### P2.3 — Grade Calculator
**Problem:** Read a numerical score between 0 and 100 and print the corresponding letter grade — A, B, C, D, or F — based on standard grade boundaries.

**Approach:**
- Map out the grade boundaries first on paper before writing any code
- Use if-elif-else with comparison operators
- Think about boundary values — does 90 get an A or a B? Define your ranges clearly before coding
- Consider what happens if the score is below 0 or above 100 — handle those as invalid input

**Tags:** Python Basics, Key Concept

---

### P2.4 — Leap Year Checker
**Problem:** Read a year and determine whether it is a leap year. A year is a leap year if it is divisible by 4, except for century years which must be divisible by 400.

**Approach:**
- The rule has three layers: divisible by 4 AND (not divisible by 100 OR divisible by 400)
- Write out the logic in plain English before translating to code
- The order and grouping of your logical operators (and, or, not) changes the result entirely
- Test with known leap years: 2000 (yes), 1900 (no), 2024 (yes)

**Tags:** HackerRank, Python Basics

---

### P2.5 — Positive, Negative, or Zero
**Problem:** Read a number and print whether it is Positive, Negative, or Zero.

**Approach:**
- Three mutually exclusive outcomes — a perfect if-elif-else structure
- The value of this problem is not the logic (it is simple) but the habit of handling all possible cases
- In every DSA problem you solve, exhaustive case handling is what separates correct from incorrect solutions

**Tags:** Python Basics

---

### P2.6 — Triangle Validity and Type Checker
**Problem:** Read three side lengths. First check if they form a valid triangle. If valid, classify it as Equilateral, Isosceles, or Scalene.

**Approach:**
- Validity rule: the sum of any two sides must be greater than the third side — check all three combinations
- Only proceed to classification if the triangle is valid
- Classification: all three sides equal = equilateral, two sides equal = isosceles, no sides equal = scalene
- This teaches nested decision making — a validity gate before the main logic

**Tags:** Python Basics, Key Concept

---

### P2.7 — Simple Calculator Using Match-Case
**Problem:** Read two numbers and an operator (+, -, *, /). Perform the corresponding operation and print the result.

**Approach:**
- Use Python's match-case statement (available from Python 3.10 onwards) to handle each operator
- Think about the division case specifically — what happens if the second number is 0? Handle it
- match-case is Python's version of switch statements found in other languages — understanding it prepares you for state machines in AI pipelines later

**Tags:** Python Basics, Key Concept

---

### P2.8 — Vowel or Consonant Checker
**Problem:** Read a single character and determine whether it is a vowel, a consonant, or neither (if it is a digit or special character).

**Approach:**
- Use the `in` operator to check membership in a string of vowels — this is cleaner than chaining multiple comparisons with `or`
- Handle uppercase and lowercase by converting the character first
- Add a check to confirm the input is actually an alphabetic character before classifying it

**Tags:** HackerRank, Python Basics

---

## Phase 3 — Strings

> **Goal:** Master string manipulation — one of the most common topics in both HackerRank and real-world ML/NLP pipelines.

---

### P3.1 — Reverse a String
**Problem:** Read a string and print it in reverse order without using Python's built-in reverse functions.

**Approach:**
- Build the reversed string character by character using a loop
- Start from the last index and work backwards — understand negative indexing
- After solving manually, compare with Python's slicing shortcut `s[::-1]`
- Understand why the manual approach matters: it is the same logic as reversing a linked list in DSA

**Tags:** HackerRank, Python Basics, Key Concept

---

### P3.2 — Count Vowels in a String
**Problem:** Read a string and count how many vowels (a, e, i, o, u) it contains. Handle both uppercase and lowercase.

**Approach:**
- Convert the entire string to lowercase first so you only need to check one case
- Loop through each character and check if it is in a vowel string using `in`
- Use a counter variable that increments each time a vowel is found
- This pattern — iterating and counting based on a condition — appears in almost every string DSA problem

**Tags:** HackerRank, Python Basics

---

### P3.3 — Check if a String is a Palindrome
**Problem:** Read a string and check whether it reads the same forwards and backwards. Print True or False.

**Approach:**
- A palindrome reads the same in both directions — "racecar", "madam"
- One approach: compare the string with its reverse
- A better approach for DSA preparation: use two pointers — one starting from the left and one from the right, moving inward and comparing characters at each step
- Stop and return False the moment a mismatch is found
- The two-pointer technique is one of the most important patterns in array and string DSA problems

**Tags:** HackerRank, LeetCode, Python Basics, Key Concept

---

### P3.4 — Caesar Cipher Encoder and Decoder
**Problem:** Read a string and a shift value k. Encode the string by shifting each letter forward by k positions in the alphabet. Letters wrap around (z shifted by 1 becomes a). Non-alphabetic characters stay unchanged.

**Approach:**
- For each character, get its ASCII value using `ord()`
- Shift it by k and wrap around using modulo 26
- Convert back to a character using `chr()`
- Handle uppercase and lowercase separately
- This problem combines string traversal, ASCII arithmetic, and modular arithmetic — all of which appear in cryptography and encoding problems in DSA

**Tags:** Python Basics, Key Concept

---

### P3.5 — Count Occurrences of a Character
**Problem:** Read a string and a character. Count how many times that character appears in the string without using the built-in `.count()` method.

**Approach:**
- Loop through every character in the string
- Compare each character with the target character
- Increment a counter on a match
- After solving manually, refactor using `.count()` and compare both approaches
- Understanding what built-in methods do internally makes you a better programmer

**Tags:** HackerRank, Python Basics

---

### P3.6 — Longest Word in a Sentence
**Problem:** Read a sentence and print the longest word in it. If there is a tie, print the first one that appears.

**Approach:**
- Split the sentence into a list of words using `.split()`
- Loop through the list, tracking the longest word seen so far
- Update your tracker only when you find a strictly longer word — this preserves the first occurrence on a tie
- After solving manually, explore using `max()` with `key=len` and understand what the `key` parameter does

**Tags:** HackerRank, Python Basics

---

### P3.7 — Check if Two Strings are Anagrams
**Problem:** Read two strings and determine whether they are anagrams of each other. Two strings are anagrams if they contain the same characters in the same frequencies, regardless of order.

**Approach:**
- One approach: sort both strings and compare — if they are equal, they are anagrams
- A better approach: count the frequency of each character in both strings using a dictionary and compare the dictionaries
- The dictionary frequency approach is O(n) — the same pattern used in many hashmap-based DSA problems

**Tags:** LeetCode, Python Basics, Key Concept

---

### P3.8 — Title Case Converter
**Problem:** Read a sentence and convert it to title case — the first letter of every word is capitalised, the rest are lowercase — without using `.title()`.

**Approach:**
- Split the sentence into words
- For each word, capitalise the first character and lowercase the rest using string slicing and concatenation
- Rejoin the words into a sentence
- This builds your understanding of string slicing which is used constantly in sliding window problems

**Tags:** Python Basics

---

## Phase 4 — Control Flow

> **Goal:** Build the habit of thinking in conditions and decision trees before writing code — the core analytical skill for breaking down any problem.

---

### P4.1 — Number Classifier
**Problem:** Read an integer and classify it in multiple ways simultaneously: positive/negative/zero, even/odd, and single-digit/double-digit/large. Print all three classifications.

**Approach:**
- Three independent classification tasks on the same input
- Write three separate if-elif-else blocks — do not try to nest them all together
- This problem teaches you to decompose a multi-part problem into independent sub-problems — the exact skill needed for DSA problem analysis

**Tags:** Python Basics, Key Concept

---

### P4.2 — Traffic Light System
**Problem:** Read a colour (Red, Yellow, Green) and print the corresponding traffic instruction. Handle invalid inputs gracefully.

**Approach:**
- Use if-elif-else or match-case
- The key lesson here is handling unexpected input — always add an else or default case
- In production ML systems and AI pipelines, unhandled edge cases cause silent failures that are very hard to debug

**Tags:** Python Basics

---

### P4.3 — Discount Calculator
**Problem:** A shop offers discounts based on purchase amount — 0% below ₹500, 10% from ₹500 to ₹1000, 20% above ₹1000. Read the purchase amount and print the final price after discount.

**Approach:**
- Identify the three tiers and their boundaries clearly before writing conditions
- Compute the discount percentage first, then apply it to the amount
- Separate the decision logic (which tier?) from the calculation logic (what is the final price?) — this separation of concerns is a fundamental software engineering principle

**Tags:** Python Basics, Key Concept

---

### P4.4 — Rock Paper Scissors
**Problem:** Read two players' choices and determine the winner, or declare a draw.

**Approach:**
- List all winning combinations for Player 1 — there are exactly three
- Check if Player 1's combination matches any winning pair
- If not, check for a draw, then Player 2 wins
- This problem teaches you to enumerate all possible states — critical for game theory and graph traversal in DSA

**Tags:** Python Basics

---

## Phase 5 — Loops

> **Goal:** Loops are the engine of every algorithm. Master them completely before moving to data structures.

---

### P5.1 — Multiplication Table of N
**Problem:** Read a number n and print its multiplication table from 1 to 10, formatted cleanly.

**Approach:**
- Use a for loop from 1 to 10 (inclusive — remember range(1, 11))
- Format each line as "n × i = result" using f-strings
- This is simple but builds the muscle memory of loop structure — index, operation, output

**Tags:** Python Basics

---

### P5.2 — Sum of Digits of a Number
**Problem:** Read an integer and print the sum of all its individual digits. For example, 1234 → 1+2+3+4 = 10.

**Approach:**
- Do not convert the number to a string — extract digits mathematically
- Use `% 10` to get the last digit and `// 10` to remove it — repeat in a while loop until the number becomes 0
- This modular digit extraction technique is used directly in number theory problems in DSA

**Tags:** HackerRank, Python Basics

---

### P5.3 — Reverse a Number
**Problem:** Read an integer and print its digits in reverse order as a number. For example, 1234 → 4321.

**Approach:**
- Again, work with the number mathematically rather than converting to a string
- Extract the last digit using `% 10`, add it to a result variable (multiplied by 10 each iteration to shift place value), then remove it using `// 10`
- Handle the edge case of trailing zeros — reversing 100 should give 1, not 001

**Tags:** Python Basics, Key Concept

---

### P5.4 — Print All Prime Numbers up to N
**Problem:** Read a number n and print all prime numbers from 2 to n.

**Approach:**
- A prime number has no divisors other than 1 and itself
- For each number from 2 to n, check if any number from 2 to its square root divides it — if none do, it is prime
- The square root optimisation is important: if a number has no divisors up to its square root, it has none beyond it either
- Understand this optimisation deeply — it directly applies to factorisation problems in DSA

**Tags:** HackerRank, Python Basics, Key Concept

---

### P5.5 — Fibonacci Sequence up to N Terms
**Problem:** Read a number n and print the first n terms of the Fibonacci sequence.

**Approach:**
- The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two before it
- Use two variables to track the last two terms — update them at each step
- Do not use recursion here — write the iterative version first
- You will revisit this with recursion in Phase 6 and compare the two approaches

**Tags:** HackerRank, LeetCode, Python Basics

---

### P5.6 — Number Pattern Printing (Pyramid)
**Problem:** Read a number n and print a right-angled triangle pattern of numbers with n rows. Row 1 has one number, row 2 has two, and so on.

**Approach:**
- Use a nested loop — the outer loop controls the row number, the inner loop controls how many numbers to print in that row
- Think about what value to print at each position — is it the row number, the column number, or something else?
- Pattern problems train your ability to think in two dimensions — the same mental model needed for 2D array and matrix problems in DSA

**Tags:** HackerRank, Python Basics

---

### P5.7 — Find All Factors of a Number
**Problem:** Read a number n and print all of its factors — numbers that divide n with no remainder.

**Approach:**
- Loop from 1 to n and collect numbers where `n % i == 0`
- Optimise: only loop to the square root of n — for each factor i found, n//i is also a factor
- Sort and print both halves together
- Factor finding is a direct prerequisite for problems involving GCD, LCM, and prime factorisation in DSA

**Tags:** Python Basics

---

### P5.8 — Strong Number Checker
**Problem:** A strong number is one where the sum of the factorials of its digits equals the number itself. For example, 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145. Read a number and check if it is a strong number.

**Approach:**
- Extract each digit using the modulo method from P5.2
- Compute the factorial of each digit — either using a nested loop or a helper function
- Sum all the factorials and compare with the original number
- This problem combines digit extraction, factorial computation, and comparison — it tests whether you can chain multiple concepts together

**Tags:** Python Basics, Key Concept

---

### P5.9 — Count Words in a Sentence
**Problem:** Read a sentence and count the total number of words in it. Handle cases where multiple spaces appear between words.

**Approach:**
- Python's `.split()` without arguments automatically handles multiple spaces — understand why
- Count the resulting list length
- Then extend it: count how many words start with a vowel, or count words longer than 4 characters
- These extensions practise filtering within iteration — a core pattern in list comprehensions and functional programming

**Tags:** Python Basics

---

### P5.10 — Bubble Sort Implementation
**Problem:** Given a list of integers, sort them in ascending order using the bubble sort algorithm. Do not use Python's built-in `sort()` or `sorted()`.

**Approach:**
- Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order
- Each full pass through the list moves the largest unsorted element to its correct position at the end
- You need n-1 passes for a list of n elements
- Add an optimisation: if no swaps occurred in a pass, the list is already sorted — stop early
- Understanding bubble sort is the gateway to understanding merge sort and quick sort

**Tags:** Python Basics, Key Concept, DSA Foundation

---

### P5.11 — Selection Sort Implementation
**Problem:** Sort a list using selection sort. In each pass, find the minimum element in the unsorted portion and place it at the beginning.

**Approach:**
- Divide the list conceptually into a sorted portion (left) and unsorted portion (right)
- In each pass, scan the unsorted portion to find the minimum element
- Swap it with the first element of the unsorted portion
- Advance the boundary between sorted and unsorted by one position
- Compare its behaviour and performance with bubble sort

**Tags:** Python Basics, Key Concept, DSA Foundation

---

## Phase 6 — Functions & Recursion

> **Goal:** Learn to decompose problems into reusable units and understand recursion — the foundation of trees, graphs, and divide-and-conquer algorithms.

---

### P6.1 — is_prime(n) Function
**Problem:** Write a reusable function that takes an integer and returns True if it is prime, False otherwise. Then use this function to print all primes up to 100.

**Approach:**
- Encapsulate the prime-checking logic you built in Phase 5 into a function
- The function should handle edge cases: numbers less than 2 are not prime
- Calling the function inside a loop to generate primes demonstrates function reuse — the same function, called many times, for different inputs

**Tags:** Python Basics, Key Concept

---

### P6.2 — Factorial — Iterative and Recursive
**Problem:** Write two versions of a factorial function — one using a loop, one using recursion. Compare their output and understand how each works.

**Approach:**
- Iterative: multiply all numbers from 1 to n using a loop
- Recursive: factorial(n) = n × factorial(n-1), with factorial(0) = 1 as the base case
- The base case is the most important part of any recursive function — without it, the function calls itself forever
- Trace through factorial(4) manually on paper to see the call stack building up and unwinding

**Tags:** HackerRank, LeetCode, Python Basics, Key Concept

---

### P6.3 — GCD and LCM of Two Numbers
**Problem:** Write functions to find the Greatest Common Divisor and Lowest Common Multiple of two numbers using the Euclidean algorithm.

**Approach:**
- The Euclidean algorithm for GCD: gcd(a, b) = gcd(b, a % b), stopping when b becomes 0
- This is naturally recursive — a function calling itself with smaller inputs each time
- LCM can be derived from GCD: LCM(a,b) = (a × b) / GCD(a,b)
- GCD is used directly in problems involving fractions, ratios, and number theory in DSA

**Tags:** HackerRank, Python Basics, Key Concept

---

### P6.4 — Binary Search — Iterative and Recursive
**Problem:** Given a sorted list and a target value, return the index of the target using binary search. Write both iterative and recursive versions.

**Approach:**
- Binary search works only on sorted lists — always state this assumption
- At each step, look at the middle element. If it equals the target, return. If the target is smaller, search the left half. If larger, search the right half.
- Each step eliminates half the remaining elements — this gives O(log n) time complexity
- This is the first algorithm where you reason about time complexity — get comfortable with this thinking
- The recursive version maps directly to how trees are searched in DSA

**Tags:** LeetCode, Python Basics, Key Concept, DSA Foundation

---

### P6.5 — Power Function Without ** Operator
**Problem:** Write a function my_pow(base, exp) that computes base to the power of exp without using the ** operator or `math.pow()`.

**Approach:**
- Simple version: multiply base by itself exp times in a loop
- Optimised version — fast exponentiation: if exp is even, my_pow(base, exp) = my_pow(base×base, exp//2). If odd, base × my_pow(base, exp-1)
- The fast exponentiation approach is O(log n) — the same divide-and-conquer thinking behind merge sort
- Trace through my_pow(2, 10) with the optimised version to see how quickly it reaches the answer

**Tags:** LeetCode, Python Basics, Key Concept

---

### P6.6 — Flatten a Nested List
**Problem:** Given a list that may contain other lists inside it, flatten it into a single list. For example, [[1,2],[3,[4,5]]] → [1,2,3,4,5].

**Approach:**
- Loop through each element — if it is a list, recurse into it; if it is not, add it to the result
- This is a natural recursive problem because the structure is self-similar — a list that may contain lists
- This pattern of checking type and recursing is used directly when traversing tree structures in DSA

**Tags:** Python Basics, Key Concept

---

### P6.7 — Generate All Subsets of a List
**Problem:** Given a list of unique integers, generate and print all possible subsets including the empty set.

**Approach:**
- A list of n elements has 2^n subsets
- Recursive approach: for each element, either include it in the current subset or exclude it — then recurse on the remaining elements
- The base case is when you have processed all elements — at that point, record the current subset
- This is the backtracking pattern — one of the most important techniques in DSA for problems involving combinations, permutations, and search spaces

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### P6.8 — Count Inversions in an Array
**Problem:** Count the number of inversions in a list — a pair (i, j) where i < j but arr[i] > arr[j]. A sorted array has 0 inversions.

**Approach:**
- Brute force: two nested loops checking every pair — O(n²)
- Efficient approach: use a modified merge sort — count inversions while merging two sorted halves
- When an element from the right half is placed before an element from the left half during merge, it forms inversions with all remaining elements in the left half
- This is the first problem where you solve something inside another algorithm — a key advanced technique

**Tags:** LeetCode, Key Concept, DSA Foundation

---

## Phase 7 — Lists

> **Goal:** Lists are Python's arrays — the most fundamental data structure in DSA. Every array problem on LeetCode starts here.

---

### P7.1 — Find Second Largest in a List
**Problem:** Given a list of integers, find the second largest value without sorting the list.

**Approach:**
- Use a single pass through the list
- Track two variables: the largest and the second largest seen so far
- Update them carefully — when you find a new largest, the old largest becomes the new second largest
- Edge case: what if all elements are the same? What if the list has fewer than 2 elements?
- Single-pass solutions are O(n) and are always preferred over sorting which is O(n log n)

**Tags:** HackerRank, Python Basics, Key Concept

---

### P7.2 — Remove Duplicates from a List
**Problem:** Given a list that may contain repeated values, return a new list with all duplicates removed while preserving the original order.

**Approach:**
- Method 1: convert to a set — fast but loses order
- Method 2: loop through the list, add to a result list only if the element has not been seen before — use a set to track seen elements in O(1)
- Method 3: use dict.fromkeys() which preserves insertion order in Python 3.7+
- Understanding all three approaches teaches you the trade-off between time complexity, space complexity, and order preservation

**Tags:** LeetCode, Python Basics, Key Concept

---

### P7.3 — Two Sum Problem
**Problem:** Given a list of integers and a target value, find and return the indices of two numbers that add up to the target. Assume exactly one solution exists.

**Approach:**
- Brute force: two nested loops checking every pair — O(n²) time
- Optimal: loop once through the list. For each element x, calculate the complement (target - x). Check if the complement is already in a dictionary. If yes, you found your pair. If no, store x with its index in the dictionary.
- This is the canonical hashmap problem — the most important pattern in array DSA problems
- Nearly every "find a pair" problem on LeetCode uses this pattern

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### P7.4 — Rotate a List by K Positions
**Problem:** Given a list and a number k, rotate the list to the right by k positions. The last k elements move to the front.

**Approach:**
- Handle k larger than the list length by using k % len(list) — rotating by the full length brings you back to the start
- Slicing approach: result = arr[-k:] + arr[:-k]
- In-place approach (important for DSA): reverse the entire array, then reverse the first k elements, then reverse the remaining elements
- The three-reversal in-place technique is O(1) space — a critical concept for memory-efficient algorithms

**Tags:** LeetCode, Python Basics, Key Concept

---

### P7.5 — Find All Pairs With a Given Sum
**Problem:** Given a list and a target sum, print all unique pairs of elements that add up to the target.

**Approach:**
- Use a set to track elements seen so far
- For each element x, check if (target - x) is in the set
- If yes, you have found a pair — print it and add both to a "used" set to avoid printing duplicates
- This is a variation of the Two Sum problem — recognising it as the same underlying pattern is the skill you are building

**Tags:** HackerRank, LeetCode, Key Concept

---

### P7.6 — Sliding Window — Maximum Sum Subarray of Size K
**Problem:** Given a list of integers and a window size k, find the subarray of size k with the maximum sum.

**Approach:**
- Brute force: compute the sum of every possible subarray of size k — O(n×k)
- Sliding window: compute the sum of the first k elements. Then slide the window one step at a time — add the new element entering the window and subtract the element leaving it — O(n)
- The sliding window technique eliminates redundant recomputation and is one of the most important patterns in array and string DSA problems

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### P7.7 — Two Pointer Sum on Sorted Array
**Problem:** Given a sorted list and a target, find two elements that sum to the target using the two-pointer technique.

**Approach:**
- Place one pointer at the start (left) and one at the end (right) of the list
- If their sum equals the target, you found the pair
- If the sum is less than the target, move the left pointer right (to increase the sum)
- If the sum is greater, move the right pointer left (to decrease the sum)
- This technique works only on sorted data and is O(n) — it is the foundation of a huge class of array problems

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### P7.8 — Group Anagrams from a List of Words
**Problem:** Given a list of words, group them so that all anagrams appear together in the same group.

**Approach:**
- For each word, compute a key that is the same for all its anagrams — sorting the characters of the word gives this key
- Use a dictionary where each key maps to a list of words that are anagrams of each other
- Append each word to the list under its sorted key
- This is a dictionary grouping pattern — used in many classification and clustering problems

**Tags:** LeetCode, Key Concept

---

### P7.9 — Merge Two Dicts Summing Common Keys
**Problem:** Given two dictionaries where values are numbers, merge them so that keys present in both dictionaries have their values summed.

**Approach:**
- Start with a copy of the first dictionary
- Iterate over the second dictionary — for each key, use `.get(key, 0)` to safely fetch the existing value with a default of 0, then add the new value
- Understanding `.get()` with a default value is a pattern used constantly in frequency counting and hashmap problems

**Tags:** Python Basics, Key Concept

---

## Phase 8 — Dictionaries & Sets

> **Goal:** Dictionaries (hash maps) and sets are the tools that turn O(n²) brute force solutions into O(n) optimal ones. Mastering them is essential for LeetCode.

---

### P8.1 — Word Frequency Counter
**Problem:** Read a paragraph of text and count how many times each unique word appears. Print the words and their frequencies sorted by frequency in descending order.

**Approach:**
- Split the text into words and convert to lowercase
- Use a dictionary to count frequencies — for each word, increment its count using `.get(word, 0) + 1`
- Sort the dictionary items by value in descending order
- This is the canonical hashmap frequency problem — you will use this pattern in NLP preprocessing for ML pipelines

**Tags:** HackerRank, Python Basics, Key Concept

---

### P8.2 — First Non-Repeating Character
**Problem:** Given a string, find and print the first character that appears exactly once. If none exists, print "None".

**Approach:**
- First pass: count the frequency of every character using a dictionary
- Second pass: go through the string in order and return the first character with a count of 1
- Two-pass approaches on strings are very common in DSA — the first pass gathers information, the second pass uses it

**Tags:** LeetCode, Key Concept

---

### P8.3 — Set Operations — Union, Intersection, Difference
**Problem:** Given two lists of numbers, compute their union, intersection, and difference using sets. Print each result.

**Approach:**
- Convert both lists to sets first
- Union: all elements from both sets — use `|` operator
- Intersection: elements common to both — use `&` operator
- Difference: elements in set A but not set B — use `-` operator
- Sets underpin graph algorithms, cycle detection, and visited-node tracking in DSA

**Tags:** Python Basics, Key Concept

---

### P8.4 — Find the Missing Number in a Sequence
**Problem:** Given a list containing n-1 numbers from 1 to n with one number missing, find the missing number.

**Approach:**
- Method 1: use the formula for the sum of first n natural numbers: n×(n+1)/2. Subtract the actual sum of the list.
- Method 2: convert the expected range to a set, convert the list to a set, and find the difference
- The formula method is O(1) space — a classic mathematical trick used in many array problems
- The set method generalises to finding multiple missing numbers

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### P8.5 — Longest Consecutive Sequence
**Problem:** Given an unsorted list of integers, find the length of the longest sequence of consecutive numbers. For example, [100, 4, 200, 1, 3, 2] → the sequence 1,2,3,4 has length 4.

**Approach:**
- Convert the list to a set for O(1) lookup
- For each number, only start counting a sequence if (number - 1) is NOT in the set — this ensures you only start from the beginning of a sequence
- Count forward from that number as long as consecutive numbers exist in the set
- Track the maximum length found
- This is a classic O(n) set problem that appears frequently on LeetCode

**Tags:** LeetCode, Key Concept, DSA Foundation

---

## Phase 9 — Tuples & Unpacking

> **Goal:** Understand immutability and Python's unpacking syntax — used everywhere in data processing and ML code.

---

### P9.1 — Student Record Sorter
**Problem:** Given a list of tuples where each tuple contains a student's name and score, sort them by score in descending order and print the ranked list.

**Approach:**
- Use `sorted()` with a `key` parameter — `key=lambda x: x[1]` extracts the score from each tuple
- Understanding lambda functions and the `key` parameter is essential — you use this pattern constantly when sorting complex data structures
- Tuples are immutable — understand what this means and why it matters for using tuples as dictionary keys

**Tags:** Python Basics, Key Concept

---

### P9.2 — Coordinate Distance Calculator
**Problem:** Given a list of coordinate pairs as tuples, calculate the distance of each point from the origin and print them sorted by distance.

**Approach:**
- Unpack each tuple into x and y coordinates
- Apply the distance formula: √(x² + y²)
- Sort the list of (distance, coordinate) pairs
- Tuple unpacking in loops — `for x, y in coordinates` — is syntax you will use constantly in ML data processing

**Tags:** Python Basics, Key Concept

---

## Phase 10 — File I/O & JSON

> **Goal:** Reading and writing files and JSON is the entry point to working with real datasets, configs, and ML pipelines.

---

### P10.1 — Word Count of a Text File
**Problem:** Read a `.txt` file, count the total number of words, and count the frequency of each unique word. Write the results to a new output file.

**Approach:**
- Use `open()` with a context manager (`with` statement) — this automatically closes the file when done
- Read the entire content, split into words, and process
- Write results to a new file using `open()` in write mode
- The `with` statement pattern is used in every file operation in production code

**Tags:** Python Basics, Key Concept

---

### P10.2 — CSV Reader and Stats Calculator
**Problem:** Read a CSV file manually (without pandas), extract a numeric column, and compute its mean, maximum, and minimum.

**Approach:**
- Open the file, read line by line, split each line by comma
- Skip the header row
- Convert the target column values to floats
- Compute statistics using loops — not built-in functions
- Understanding raw file parsing prepares you for when pandas is unavailable or too slow

**Tags:** Python Basics, Key Concept

---

### P10.3 — JSON Config Reader and Writer
**Problem:** Read a configuration from a `.json` file, modify a specific value, and write the updated config back to the file.

**Approach:**
- Use Python's built-in `json` module — `json.load()` to read, `json.dump()` to write
- Modify the resulting Python dictionary as normal
- Write it back with `indent=2` for readable formatting
- JSON config files are used in every ML training pipeline, RAG system, and LangGraph agent configuration

**Tags:** Python Basics, Key Concept

---

### P10.4 — To-Do List with File Persistence
**Problem:** Build a command-line to-do list where tasks are saved to a `.txt` file so they persist between program runs. Support adding, listing, and marking tasks as done.

**Approach:**
- On startup, read existing tasks from the file into a list
- Present a menu loop using a while loop
- On every change, write the updated list back to the file
- This is your first stateful application — it combines loops, functions, conditionals, and file I/O into one program

**Tags:** Python Basics, Key Concept

---

## Phase 11 — OOP (Object-Oriented Programming)

> **Goal:** OOP is how all serious Python code is structured — ML models, LangChain agents, RAG pipelines, and FastAPI services are all built with classes.

---

### P11.1 — BankAccount Class
**Problem:** Build a BankAccount class with an account holder name and balance. Implement deposit(), withdraw() (with overdraft protection), and get_balance() methods.

**Approach:**
- Define `__init__` to initialise the name and balance attributes
- Deposit simply adds to the balance
- Withdraw checks if the amount exceeds the balance before deducting
- Add a `__str__` method so printing the account object gives useful information
- This is your first complete class — understand the relationship between the object (instance) and the class (blueprint)

**Tags:** Python Basics, Key Concept

---

### P11.2 — Student Grade Tracker
**Problem:** Build a Student class that stores a name and a list of grades. Implement methods to add a grade, compute the average, and return the highest and lowest grades.

**Approach:**
- The grades list is initialised as an empty list in `__init__` — understand why you must not use a mutable default argument
- Each method performs one clear task — this is the single responsibility principle
- Add a method that returns the letter grade based on the average
- This OOP structure is exactly how ML experiment trackers store metrics per run

**Tags:** Python Basics, Key Concept

---

### P11.3 — Stack Implementation Using a Class
**Problem:** Implement a Stack data structure using a class with push(), pop(), peek(), is_empty(), and size() methods.

**Approach:**
- Use a Python list as the internal storage — the top of the stack is the end of the list
- push() appends to the end, pop() removes from the end — both O(1) operations
- peek() returns the last element without removing it
- Raise an appropriate error if pop() or peek() is called on an empty stack
- This is your first custom data structure — the direct foundation of DSA

**Tags:** Python Basics, Key Concept, DSA Foundation

---

### P11.4 — Library Book System
**Problem:** Build a Book class and a Library class. The Library manages a collection of books with methods to add a book, remove a book, search by title, and list all available books.

**Approach:**
- Book class: title, author, ISBN, available (boolean)
- Library class: stores a list of Book objects
- Search iterates through the list and compares titles
- This models a real-world has-a relationship between Library and Book — a foundational OOP concept
- The search pattern here is linear search — you will replace it with hash-based lookup in DSA

**Tags:** Python Basics, Key Concept

---

## Phase 12 — Error Handling

> **Goal:** Writing code that handles failure gracefully is what separates beginner scripts from production-ready systems.

---

### P12.1 — Safe Division Function
**Problem:** Write a function that divides two numbers but handles division by zero, invalid input types, and returns a meaningful error message for each case.

**Approach:**
- Wrap the division in a try-except block
- Catch `ZeroDivisionError` specifically, then `TypeError` for invalid types, then a general `Exception` as a final catch-all
- Return None or raise a custom exception — understand the difference between the two approaches
- Every function in a production ML pipeline must handle errors — silent failures cause data corruption

**Tags:** Python Basics, Key Concept

---

### P12.2 — Robust File Reader
**Problem:** Write a function that reads a file and returns its contents. Handle the case where the file does not exist, where permission is denied, and where the file is empty.

**Approach:**
- Catch `FileNotFoundError` and `PermissionError` specifically
- Use the `finally` block to ensure the file is always closed — or use a `with` statement which handles this automatically
- Return an empty string for an empty file rather than crashing
- This robust file reading pattern is used in every data ingestion pipeline

**Tags:** Python Basics, Key Concept

---

### P12.3 — Input Validation Loop
**Problem:** Write a program that repeatedly asks the user for a positive integer until they provide one. Handle non-numeric input and negative numbers with clear error messages.

**Approach:**
- Use a while True loop that only breaks when valid input is received
- Wrap the `int()` conversion in a try-except to catch `ValueError` when the user types text
- Add a separate check for negative numbers after the type conversion succeeds
- This validation loop pattern appears in every interactive application and command-line tool

**Tags:** Python Basics, Key Concept

---

## DSA Bridge Problems

> These 8 problems are added specifically to prepare you for Data Structures and Algorithms. Solve them after completing all phases above.

---

### B1 — Recursive Binary Search
**Problem:** Implement binary search recursively. The function takes a sorted list, a target, and the left and right boundary indices. Return the index of the target or -1 if not found.

**Approach:**
- Base case: if left > right, the target is not in the list — return -1
- Compute the middle index: mid = (left + right) // 2
- If the target equals the middle element, return mid
- If the target is less, recurse on the left half
- If the target is greater, recurse on the right half
- Trace through a small example on paper to see the recursive calls

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### B2 — Check Balanced Parentheses
**Problem:** Given a string containing only brackets — (, ), [, ], {, } — determine whether the brackets are balanced and correctly nested.

**Approach:**
- Use a stack — push every opening bracket onto the stack
- When you encounter a closing bracket, check if the top of the stack is the matching opener — if yes, pop it; if no, the string is unbalanced
- At the end, if the stack is empty the string is balanced — otherwise it is not
- This is the classic stack application problem and appears in virtually every DSA course and interview

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### B3 — Merge Sort Implementation
**Problem:** Sort a list using the merge sort algorithm. Do not use any built-in sort functions.

**Approach:**
- Divide: split the list in half recursively until each sublist has one element (a list of one element is always sorted)
- Conquer: merge two sorted sublists into one sorted list by repeatedly taking the smaller of the two front elements
- The merge step is where the actual sorting happens — understand it thoroughly
- Merge sort is O(n log n) and is stable — it is the algorithm Python's own sort is based on

**Tags:** LeetCode, Key Concept, DSA Foundation

---

### B4 — Sliding Window — Longest Substring Without Repeating Characters
**Problem:** Given a string, find the length of the longest substring that contains no repeating characters.

**Approach:**
- Use a sliding window with two pointers: left and right
- Expand the right pointer one character at a time
- Use a set to track characters currently in the window
- When a repeating character is found, shrink the window from the left until the duplicate is removed
- Track the maximum window size seen at any point
- This is one of the most commonly asked sliding window problems on LeetCode

**Tags:** LeetCode, Key Concept, DSA Foundation

---

*End of problem list. Total: 68 problems across 12 phases + 4 DSA bridge problems.*

---

## How to Approach Any Problem

1. **Read the problem twice** — once for the big picture, once for the details
2. **Identify the input and output** — write them down explicitly
3. **List the edge cases** — empty input, negative numbers, duplicates, zero
4. **Solve it manually** on paper with a small example
5. **Translate your manual steps** into pseudocode
6. **Write the code** from your pseudocode
7. **Test with your edge cases** before submitting
