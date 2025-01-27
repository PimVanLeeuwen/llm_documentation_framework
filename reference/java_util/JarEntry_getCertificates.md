#### getCertificates

```
public Certificate[] getCertificates()
```
Returns the `Certificate` objects for this entry, or
`null` if none. This method can only be called once
the `JarEntry` has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return `null`.The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).
Returns:
the `Certificate` objects for this entry, or
`null` if none.

