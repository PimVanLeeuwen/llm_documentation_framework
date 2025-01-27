#### close

```
public void close()
```
Closes this scanner.If this scanner has not yet been closed then if its underlying
readable also implements the `Closeable` interface then the readable's close method
will be invoked. If this scanner is already closed then invoking this
method will have no effect.Attempting to perform search operations after a scanner has
been closed will result in an `IllegalStateException`.
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `AutoCloseable`

