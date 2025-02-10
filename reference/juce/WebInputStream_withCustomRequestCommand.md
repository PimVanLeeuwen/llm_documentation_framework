#### withCustomRequestCommand()


 WebInputStream & WebInputStream::withCustomRequestCommand ( const String & customRequestCommand ) 
 

Override the HTTP command that is sent.Returns a reference to itself so that several methods can be chained.Note that this command will not change the way parameters are sent. This must be specified in the constructor.Parameters

 customRequestCommand this string is the custom HTTP request command such as POST or GET.