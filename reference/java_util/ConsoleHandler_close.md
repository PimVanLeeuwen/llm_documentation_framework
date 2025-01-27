#### close

```
public void close()
```
Override StreamHandler.close to do a flush but not
to close the output stream. That is, we do not
close System.err.
Overrides:
`close` in class `StreamHandler`




