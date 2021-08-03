def isPalindrome(aList):
      return aList == aList[::-1]
  
listA = [ 5, 7, 3, 22, 15, 6, 15, 22, 3, 7, 5 ]         # is palindrome
listB = [ 5, 7, 3, 22, 15, 6, 6, 15, 22, 3, 7, 5 ]      # is palindrome
listC = [ 5, 7, 3, 22, 15, 6, 7, 15, 22, 3, 7, 5 ]      # is NOT palindrome
listD = [ 5, 7, 3, 'A', 15, 'Z', 15, 'G', 3, 7, 5 ]     # is NOT palindrome
listE = [ 5, 'A', 3, 'G', 15, 6, 15, 'G', 3, 'A', 5 ]   # is palindrome

print( isPalindrome(listA) )
print( isPalindrome(listB) )
print( isPalindrome(listC) )
print( isPalindrome(listD) )
print( isPalindrome(listE) )
