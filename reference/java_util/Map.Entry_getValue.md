#### getValue

```
V getValue()
```
Returns the value corresponding to this entry. If the mapping
has been removed from the backing map (by the iterator's
remove operation), the results of this call are undefined.
Returns:
the value corresponding to this entry
Throws:
`IllegalStateException` - implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

