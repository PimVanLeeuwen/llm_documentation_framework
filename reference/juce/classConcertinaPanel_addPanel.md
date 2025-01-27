#### addPanel()


 void ConcertinaPanel::addPanel ( int insertIndex, 
 
 Component \* component, 
 bool takeOwnership ) 

Adds a component to the panel.Parameters

 insertIndex the index at which this component will be inserted, or 1 to append it to the end of the list. 
 
 component the component that will be shown 
 takeOwnership if true, then the ConcertinaPanel will take ownership of the content component, and will delete it later when it's no longer needed. If false, it won't delete it, and you must make sure it doesn't get deleted while in use.