#### equals()


 bool var::equals ( const var & other ) const noexcept 
 

Returns true if this var has the same value as the one supplied.Note that this ignores the type, so a string var "123" and an integer var with the value 123 are considered to be equal.Note that equality checking depends on the "wrapped" type of the object on which equals() is called. That means the following code will convert the righthandside argument to a string and compare the string values, because the object on the lefthandside was initialised from a string:var ("123").equals (var (123)) 
varA variant class, that can be used to hold a range of primitive values.Definition juce\_Variant.h:57
var::varvar() noexceptCreates a void variant.
However, the following code will convert the righthandside argument to a double and compare the values as doubles, because the object on the lefthandside was initialised from a double:var (45.6).equals ("45.6000") 
See alsoequalsWithSameType