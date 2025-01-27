#### launchAsynchronously()


 static CallOutBox & CallOutBox::launchAsynchronously ( std::unique\_ptr< Component > contentComponent, Rectangle< int > areaToPointTo, Component \* parentComponent ) static 
 

This will launch a callout box containing the given content, pointing to the specified target component.This method will create and display a callout, returning immediately, after which the box will continue to run modally until the user clicks on some other component, at which point it will be dismissed and deleted automatically.It returns a reference to the newlycreated box so that you can customise it, but don't keep a pointer to it, as it'll be deleted at some point when it gets closed.Parameters

 contentComponent the component to display inside the callout. This should already have a size set (although the callout will also update itself when the component's size is changed later). 
 
 areaToPointTo the area that the callout's arrow should point towards. If a parentComponent is supplied, then this is relative to that parent; otherwise, it's a global screen coord. 
 parentComponent if not a nullptr, this is the component to add the callout to. If this is a nullptr, the callout will be added to the desktop.