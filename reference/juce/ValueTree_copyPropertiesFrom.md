#### copyPropertiesFrom()


 void ValueTree::copyPropertiesFrom ( const ValueTree & source, 
 
 UndoManager \* undoManager ) 

Overwrites all the properties in this tree with the properties of the source tree.Any properties that already exist will be updated; and new ones will be added, and any that are not present in the source tree will be removed.See alsocopyPropertiesAndChildrenFrom