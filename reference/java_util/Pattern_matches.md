#### matches

```
public static boolean matches(String regex,
                              CharSequence input)
```
Compiles the given regular expression and attempts to match the given
input against it.An invocation of this convenience method of the form
```

 Pattern.matches(regex, input);
```
behaves in exactly the same way as the expression
```

 Pattern.compile(regex).matcher(input).matches()
```
If a pattern is to be used multiple times, compiling it once and reusing
it will be more efficient than invoking this method each time.
Parameters:
`regex` - The expression to be compiled
`input` - The character sequence to be matched
Returns:
whether or not the regular expression matches on the input
Throws:
`PatternSyntaxException` - If the expression's syntax is invalid

