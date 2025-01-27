#### setDataReceiver()


 void AudioFormatWriter::ThreadedWriter::setDataReceiver ( IncomingDataReceiver \* ) 
 

Allows you to specify a callback that this writer should update with the incoming data.The receiver will be cleared and the writer will begin adding data to it as the data arrives. Pass a null pointer to remove the current receiver.The object passedin must not be deleted while this writer is still using it.