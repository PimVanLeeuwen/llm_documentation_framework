#### setConnectedEdges()


 void Button::setConnectedEdges ( int connectedEdgeFlags ) 
 

Hints about which edges of the button might be connected to adjoining buttons.The value passed in is a bitwise combination of any of the values in the ConnectedEdgeFlags enum.E.g. if you are placing two buttons adjacent to each other, you could use this to indicate which edges are touching, and the LookAndFeel might choose to drawn them without rounded corners on the edges that connect. It's only a hint, so the LookAndFeel can choose to ignore it if it's not relevant for this type of button.