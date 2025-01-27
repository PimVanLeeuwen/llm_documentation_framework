#### setExtraComponent()


 void TabBarButton::setExtraComponent ( Component \* extraTabComponent, 
 
 ExtraComponentPlacement extraComponentPlacement ) 

Sets an extra component that will be shown in the tab.This optional component will be positioned inside the tab, either to the left or right of the text. You could use this to implement things like a close button or a graphical status indicator. If a nonnull component is passedin, the TabbedButtonBar will take ownership of it and delete it when required.