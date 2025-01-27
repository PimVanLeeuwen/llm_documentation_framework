#### paint()


 void SidePanel::paint ( Graphics & g ) overridevirtual 
 

Components can override this method to draw their content.The paint() method gets called when a region of a component needs redrawing, either because the component's repaint() method has been called, or because something has happened on the screen that means a section of a window needs to be redrawn.Any child components will draw themselves over whatever this method draws. If you need to paint over the top of your child components, you can also implement the paintOverChildren() method to do this.If you want to cause a component to redraw itself, this is done asynchronously calling the repaint() method marks a region of the component as "dirty", and the paint() method will automatically be called sometime later, by the message thread, to paint any bits that need refreshing. In JUCE (and almost all modern UI frameworks), you never redraw something synchronously.You should never need to call this method directly to take a snapshot of the component you could use createComponentSnapshot() or paintEntireComponent().Parameters

 g the graphics context that must be used to do the drawing operations. 
 



See alsorepaint, paintOverChildren, Graphics Reimplemented from Component.