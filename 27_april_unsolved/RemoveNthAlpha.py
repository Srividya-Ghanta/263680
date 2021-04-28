def remove_nth(string, n):
      a = string[:n] 
      b = string[n+1:]
      return a + b
print(remove_nth(input("Enter the string : "), int(input("Enter the index : "))))