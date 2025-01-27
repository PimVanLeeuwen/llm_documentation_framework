#### compile

```
public static Pattern compile(String regex,
                              int flags)
```
Compiles the given regular expression into a pattern with the given
flags.
Parameters:
`regex` - The expression to be compiled
`flags` - Match flags, a bit mask that may include
`CASE_INSENSITIVE`, `MULTILINE`, `DOTALL`,
`UNICODE_CASE`, `CANON_EQ`, `UNIX_LINES`,
`LITERAL`, `UNICODE_CHARACTER_CLASS`
and `COMMENTS`
Returns:
the given regular expression compiled into a pattern with the given flags
Throws:
`IllegalArgumentException` - If bit values other than those corresponding to the defined
match flags are set in flags
`PatternSyntaxException` - If the expression's syntax is invalid

