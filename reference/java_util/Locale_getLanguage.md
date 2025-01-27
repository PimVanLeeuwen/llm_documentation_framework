#### getLanguage

```
public String getLanguage()
```
Returns the language code of this Locale.Note: ISO 639 is not a stable standard— some languages' codes have changed.
Locale's constructor recognizes both the new and the old codes for the languages
whose codes have changed, but this function always returns the old code. If you
want to check for a specific language whose code has changed, don't do
```

 if (locale.getLanguage().equals("he")) // BAD!
    ...
 
```
Instead, do
```

 if (locale.getLanguage().equals(new Locale("he").getLanguage()))
    ...
 
```

Returns:
The language code, or the empty string if none is defined.
See Also:
`getDisplayLanguage()`

