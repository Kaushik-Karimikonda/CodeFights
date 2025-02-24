def sortByLength(inputArray):
    return sorted(inputArray,key = lambda x: len(x))

'''Given an array of strings, sort them in the order of increasing lengths. If two strings have the same length, their relative order must be the same as in the initial array.

Example

For

inputArray = ["abc",
              "",
              "aaa",
              "a",
              "zz"]
the output should be

sortByLength(inputArray) = ["",
                            "a",
                            "zz",
                            "abc",
                            "aaa"]
Input/Output

[time limit] 4000ms (py)
[input] array.string inputArray

A non-empty array of strings.

Constraints:
3 ≤ inputArray.length ≤ 10,
0 ≤ inputArray[i].length ≤ 10.

[output] array.string'''
