#### getCurrentlyModalComponent()


 static Component \*JUCE\_CALLTYPE Component::getCurrentlyModalComponent ( int index = 0 ) staticnoexcept 
 

Returns one of the components that are currently modal.The index specifies which of the possible modal components to return. The order of the components in this list is the reverse of the order in which they became modal so the component at index 0 is always the active component, and the others are progressively earlier ones that are themselves now blocked by later ones.Returnsthe modal component, or null if no components are modal (or if the index is out of range) 
See alsogetNumCurrentlyModalComponents, runModalLoop, isCurrentlyModal