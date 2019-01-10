'''
The Challenge
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
Learning objectives
This question gives you the chance to practice with algorithms and data structures. It’s also a good example of why careful analysis for Big-O performance is often worthwhile, as is careful exploration of common and worst-case input conditions.
'''

S = "abppplee"
D = ("able", "ale", "apple", "bale", "kangaroo", "abppplee")


def remove_first_occurence(S, element):
  for i,v in enumerate(S):
    if  v == element:
      S = S[i+1:]
      print(f"S={S}")
      return S
  return False


def is_subseq(S,D):
  for element in D:
    S = remove_first_occurence(S, element)
    if S == False:
      return False
  return True


def main():
  longest = False
  for element in D:
    if is_subseq(S,element):
      print(f"{element} is a substring {S}")
      if longest and len(longest) < len(element):
        longest = element
      elif not longest:
        longest = element
  print(longest)


if __name__ == "__main__":
  main()
#   print(is_subseq("abcdef", "def"))
#   print(is_subseq("computer", "muter"))
#   print(is_subseq("stringmatchingmat", "ingmat"))
#   print(is_subseq("videobox", "videobox"))
