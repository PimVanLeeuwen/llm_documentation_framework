#### move()


 void StringArray::move ( int currentIndex, int newIndex ) noexcept 
 

Moves one of the strings to a different position.This will move the string to a specified index, shuffling along any intervening elements as required.So for example, if you have the array { 0, 1, 2, 3, 4, 5 } then calling move (2, 4) would result in { 0, 1, 3, 4, 2, 5 }.Parameters

 currentIndex the index of the value to be moved. If this isn't a valid index, then nothing will be done 
 
 newIndex the index at which you'd like this value to end up. If this is less than zero, the value will be moved to the end of the array