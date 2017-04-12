# ClientServerPython
Client-Server application in python
1.    HTTP Server module
Used to receive and store text messages internally in queues and send them back to clients upon request.
 
Recieve 2 request types (non-conformant messages must be ignored):
1.1 POST request to receive text message from client and store it internally in aliased queues:
- text message value is mandatory and non-empty
- queue alias is a number from '0' to '10000'
- queue alias is optional (default value is '0')
- server module supports up to 100 different queues
- server return notification, if the target queue is fulll (has more than 100 messages)
1.2. GET request to retrieve and return oldest message from the internal message queue:
- queue alias is a number from '0' to '10000'
- queue alias is optional (default value is '0')
- oldest message is returned to client and deleted afterwards
- if there is no message in the queue, server return notification
 
2.    HTTP Client module
Used to send text messages to server and print text messages retrieved from the server using command line API with POST/GET request based implementation.
 
Support sending 2 request types:
2.1. POST request to add client-provided text message to the aliased queue:
- text message value is mandatory and non-empty
- queue alias is a number from '0' to '10000'
- queue alias is optional (default value is '0')
2.2. GET request that retrieves and prints oldest message from the queue by its alias:
- message is printed to standard output
- queue alias is a number from '0' to '10000'
- queue alias is optional (default value is '0')
3.    Automated test suite covering functional requirements.
