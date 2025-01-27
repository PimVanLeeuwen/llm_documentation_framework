#### orElseThrow

```
public <X extends Throwable> T orElseThrow(Supplier<? extends X> exceptionSupplier)
                                    throws X
```
Return the contained value, if present, otherwise throw an exception
to be created by the provided supplier.
API Note:
A method reference to the exception constructor with an empty
argument list can be used as the supplier. For example,
`IllegalStateException::new`
Type Parameters:
`X` - Type of the exception to be thrown
Parameters:
`exceptionSupplier` - The supplier which will return the exception to
be thrown
Returns:
the present value
Throws:
`X` - if there is no value present
`NullPointerException` - if no value is present and
`exceptionSupplier` is null
`X extends Throwable`

