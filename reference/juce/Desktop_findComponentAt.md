#### findComponentAt()


 Component \* Desktop::findComponentAt ( Point< int > screenPosition ) const 
 

Finds the component at a given screen location.This will drill down into toplevel windows to find the child component at the given position.Returns nullptr if the coordinates are inside a nonJUCE window.