from code_516_longest_palindromic_sequence import Solution

def test_example_1():
    s = Solution()
    s1 = "bbbab"
    output = 4
    assert s.longestPalindromeSubseq(s1) == output

def test_example_2():
    s = Solution()
    s1 = "aaa"
    output = 3
    assert s.longestPalindromeSubseq(s1) == output