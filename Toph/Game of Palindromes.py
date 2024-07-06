def count_palindromic_substrings(s):
    n = len(s)
    count = 0
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check for 2-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1
    
    # Check for palindromes longer than 2 characters
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1
    
    return count

def lannister_ratio(s):
    total_substrings = len(s) * (len(s) + 1) // 2
    palindromic_substrings = count_palindromic_substrings(s)
    return palindromic_substrings / total_substrings

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    results = []
    for i in range(1, n + 1):
        ratio = lannister_ratio(data[i])
        results.append(f"{ratio:.3f}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
