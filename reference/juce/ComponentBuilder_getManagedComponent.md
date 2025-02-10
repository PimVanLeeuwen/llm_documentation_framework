#### getManagedComponent()


 Component \* ComponentBuilder::getManagedComponent ( ) 
 

Returns the builder's component (creating it if necessary).The first time that this method is called, the builder will attempt to create a component from the ValueTree, so you must have registered some suitable type handlers before calling this. If there's a problem and the component can't be created, this method returns nullptr.The component that is returned is owned by this ComponentBuilder, so you can put it inside your own parent components, but don't delete it! The ComponentBuilder will delete it automatically when the builder is destroyed. If you want to get a component that you can delete yourself, call createComponent() instead.The ComponentBuilder will update this component if any changes are made to the ValueTree, so if there's a chance that the tree might change, be careful not to keep any pointers to subcomponents, as they may be changed or removed.