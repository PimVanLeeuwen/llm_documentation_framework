#### available

```
public int available()
              throws IOException
```
Returns 0 after EOF has been reached, otherwise always return 1.Programs should not count on this method to return the actual number
of bytes that could be read without blocking.
Overrides:
`available` in class `FilterInputStream`
Returns:
1 before EOF and 0 after EOF.
Throws:
`IOException` - if an I/O error occurs.

