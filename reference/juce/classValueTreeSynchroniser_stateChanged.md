#### stateChanged()


 virtual void ValueTreeSynchroniser::stateChanged ( const void \* encodedChange, size\_t encodedChangeSize ) pure virtual 
 

This callback happens when the ValueTree changes and the given statechange message needs to be applied to any other trees that need to stay in sync with it.The data is an opaque blob of binary that you should transmit to wherever your target tree lives, and use applyChange() to apply this to the target tree.