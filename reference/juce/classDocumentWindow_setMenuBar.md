#### setMenuBar()


 void DocumentWindow::setMenuBar ( MenuBarModel \* menuBarModel, 
 
 int menuBarHeight = 0 ) 

Creates a menu inside this window.Parameters

 menuBarModel this specifies a MenuBarModel that should be used to generate the contents of a menu bar that will be placed just below the title bar, and just above any content component. If this value is a nullptr, any existing menu bar will be removed from the component; if it is not a nullptr, one will be added if it's required. 
 
 menuBarHeight the height of the menu bar component, if one is needed. Pass a value of zero or less to use the lookandfeel's default size.