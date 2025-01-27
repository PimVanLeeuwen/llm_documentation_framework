#### getCodeSigners

```
public CodeSigner[] getCodeSigners()
```
Returns the `CodeSigner` objects for this entry, or
`null` if none. This method can only be called once
the `JarEntry` has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return `null`.The returned array comprises all the code signers that have signed
this entry.
Returns:
the `CodeSigner` objects for this entry, or
`null` if none.
Since:
1.5




