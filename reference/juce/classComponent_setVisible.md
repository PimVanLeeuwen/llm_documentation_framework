#### setVisible()


 virtual void Component::setVisible ( bool shouldBeVisible ) virtual 
 

Makes the component visible or invisible.This method will show or hide the component. Note that components default to being nonvisible when first created. Also note that visible components won't be seen unless all their parent components are also visible.This method will call visibilityChanged() and also componentVisibilityChanged() for any component listeners that are interested in this component.Parameters

 shouldBeVisible whether to show or hide the component 
 



See alsoisVisible, isShowing, visibilityChanged, ComponentListener::componentVisibilityChanged Reimplemented in ScrollBar.Referenced by LassoComponent< SelectableItemType >::dragLasso(), and LassoComponent< SelectableItemType >::endLasso().