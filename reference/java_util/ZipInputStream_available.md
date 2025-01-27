#### available

```
public int available()
              throws IOException
```
Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.Programs should not count on this method to return the actual number
of bytes that could be read without blocking.
Overrides:
`available` in class `InflaterInputStream`
Returns:
1 before EOF and 0 after EOF has reached for current entry.
Throws:
`IOException` - if an I/O error occurs.

