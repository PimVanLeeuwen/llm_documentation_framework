#### createComponent()


 Component \* ComponentBuilder::createComponent ( ) 
 

Creates and returns a new instance of the component that the ValueTree represents.The caller is responsible for using and deleting the object that is returned. Unlike getManagedComponent(), the component that is returned will not be updated by the builder.