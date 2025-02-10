#### findFirstTargetParentComponent()


 ApplicationCommandTarget \* ApplicationCommandTarget::findFirstTargetParentComponent ( ) 
 

If this object is a Component, this method will search upwards in its current UI hierarchy for the next parent component that implements the ApplicationCommandTarget class.If your target is a Component, this is a very handy method to use in your getNextCommandTarget() implementation.