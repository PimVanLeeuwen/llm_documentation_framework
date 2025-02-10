#### moveChild()


 void ValueTree::moveChild ( int currentIndex, 
 
 int newIndex, 
 UndoManager \* undoManager ) 

Moves one of the subtrees to a different index.This will move the child to a specified index, shuffling along any intervening items as required. So for example, if you have a list of { 0, 1, 2, 3, 4, 5 }, then calling move (2, 4) would result in { 0, 1, 3, 4, 2, 5 }.Parameters

 currentIndex the index of the item to be moved. If this isn't a valid index, then nothing will be done 
 
 newIndex the index at which you'd like this item to end up. If this is less than zero, the value will be moved to the end of the list 
 undoManager the optional UndoManager to use to store this transaction