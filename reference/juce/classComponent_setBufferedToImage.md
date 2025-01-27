#### setBufferedToImage()


 void Component::setBufferedToImage ( bool shouldBeBuffered ) 
 

Makes the component use an internal buffer to optimise its redrawing.Setting this flag to true will cause the component to allocate an internal buffer into which it paints itself and all its child components, so that when asked to redraw itself, it can use this buffer rather than actually calling the paint() method.Parts of the buffer are invalidated when repaint() is called on this component or its children. The buffer is then repainted at the next paint() callback.See alsorepaint, paint, createComponentSnapshot