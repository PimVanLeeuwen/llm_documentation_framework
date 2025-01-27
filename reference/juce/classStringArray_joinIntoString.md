#### joinIntoString()


 String StringArray::joinIntoString ( StringRef separatorString, 
 
 int startIndex = 0, 
 int numberOfElements = 1 ) const 

Joins the strings in the array together into one string.This will join a range of elements from the array into a string, separating them with a given string.e.g. joinIntoString (",") will turn an array of "a" "b" and "c" into "a,b,c".Parameters

 separatorString the string to insert between all the strings 
 
 startIndex the first element to join 
 numberOfElements how many elements to join together. If this is less than zero, all available elements will be used.