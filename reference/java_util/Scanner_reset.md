#### reset

```
public Scanner reset()
```
Resets this scanner.Resetting a scanner discards all of its explicit state
information which may have been changed by invocations of `useDelimiter(java.util.regex.Pattern)`, `useLocale(java.util.Locale)`, or `useRadix(int)`.An invocation of this method of the form
scanner.reset() behaves in exactly the same way as the
invocation
```

   scanner.useDelimiter("\\p{javaWhitespace}+")
          .useLocale(Locale.getDefault(Locale.Category.FORMAT))
          .useRadix(10);
 
```

Returns:
this scanner
Since:
1.6




