#### setDictionary

```
public void setDictionary(byte[] b)
```
Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.
Parameters:
`b` - the dictionary data bytes
See Also:
`needsDictionary()`,
`getAdler()`

