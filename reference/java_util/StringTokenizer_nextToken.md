#### nextToken

```
public String nextToken(String delim)
```
Returns the next token in this string tokenizer's string. First,
the set of characters considered to be delimiters by this
StringTokenizer object is changed to be the characters in
the string delim. Then the next token in the string
after the current position is returned. The current position is
advanced beyond the recognized token. The new delimiter set
remains the default after this call.
Parameters:
`delim` - the new delimiters.
Returns:
the next token, after switching to the new delimiter set.
Throws:
`NoSuchElementException` - if there are no more tokens in this
tokenizer's string.
`NullPointerException` - if delim is `null`

