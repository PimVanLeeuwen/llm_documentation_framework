#### getCreationTime

```
public FileTime getCreationTime()
```
Returns the creation time of the entry.The creation time is from the extended timestamp fields of
entry's `optional extra data` when read from a ZIP file
or ZIP file formatted stream.
Returns:
the creation time of the entry, null if not specified
Since:
1.8
See Also:
`setCreationTime(FileTime)`

