#### replaceFirst

```
public String replaceFirst(String replacement)
```
Replaces the first subsequence of the input sequence that matches the
pattern with the given replacement string.This method first resets this matcher. It then scans the input
sequence looking for a match of the pattern. Characters that are not
part of the match are appended directly to the result string; the match
is replaced in the result by the replacement string. The replacement
string may contain references to captured subsequences as in the `appendReplacement` method.Note that backslashes (\) and dollar signs ($) in
the replacement string may cause the results to be different than if it
were being treated as a literal replacement string. Dollar signs may be
treated as references to captured subsequences as described above, and
backslashes are used to escape literal characters in the replacement
string.Given the regular expression dog, the input
"zzzdogzzzdogzzz", and the replacement string
"cat", an invocation of this method on a matcher for that
expression would yield the string "zzzcatzzzdogzzz".Invoking this method changes this matcher's state. If the matcher
is to be used in further matching operations then it should first be
reset.
Parameters:
`replacement` - The replacement string
Returns:
The string constructed by replacing the first matching
subsequence by the replacement string, substituting captured
subsequences as needed

