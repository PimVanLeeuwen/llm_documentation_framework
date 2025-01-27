#### runAndReset

```
protected boolean runAndReset()
```
Executes the computation without setting its result, and then
resets this future to initial state, failing to do so if the
computation encounters an exception or is cancelled. This is
designed for use with tasks that intrinsically execute more
than once.
Returns:
`true` if successfully run and reset




