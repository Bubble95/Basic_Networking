import socket, os, json, pdb

class Client:
    """ This class allwos the user to connect to a server by using the method: connect()
    """
 
    #constructor + Type hinting adr:str appears whe creating object
    def __init__(self,adr: str, port: int):
        """Arguments:
            adr:  str - Name of domain or IP
            port: int _ between 0 and 65535
        """
        self.adr     = adr
        self.port   = port
        try: 
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.settimeout(5.0)
        except Exception as err:
            print(err) #print Exception to terminal
            return
   
    def get_file(self):
        """
            Receives a file from given server
        """

        # resolve hostname
        if type(self.adr) is not str: #raise exception if adr is not string
            raise Exception('adr must be of type String')    
        try:
            ip = socket.gethostbyname(self.adr)
        except Exception as err:
            print('Exception using socket.gethostbyname():\n', err)
            return
        #try to connect to destination
        if type(self.port) is not int: #raise exception if port is not int
            raise Exception('ip must be of type integer')
        elif self.port < 0 or self.port > 65535:
            raise Exception('Port must be between 0 and 65535')
        try:
            self.s.connect((ip,self.port))
            print('connected to: %s\n' %(ip))
        except Exception as err:
            print(err)
            self.s.close()
            return
        try:
            msg = self.s.recv(4096).decode()
                        
        except Exception as err:
            print('self.c.recv(size)\n', err)
        self.s.close()
        fileJson = json.loads(msg)
        file = open(fileJson['name']+'copy.txt','w')
        file.write(fileJson['content'])
        file.close()
        return fileJson

class Server:

    def __init__(self,adr: str, port: int):
        self.port = port
        self.adr  = adr
        try: 
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as err:
            print(err) #print Exception to terminal
            return

    def launch(self):
        if type(self.adr) is not str: #raise exception if adr is not string
            raise Exception('adr must be of type String')
        if type(self.port) is not int: #raise exception if port is not int
            raise Exception('ip must be of type integer')
        elif self.port < 0 or self.port > 65535:
            raise Exception('Port must be between 0 and 65535')
        try:
            self.s.bind((self.adr, self.port))
            print("socket binded to %s" %(self.port))
        except Exception as err:
            print('Exception cathed when executing self.s.bind((adr,port))\n',err)
            return
        # put the socket into listening mode - 5 scokets can be in queue, 6th is refused
        try:
            self.s.listen(5)
            print("socket is listening\n")
        except Exception as err:
            print('self.s.listen(5)',err)
            return

    def send_file(self, fileName: str):

        if type(fileName) is not str:
            raise Exception('fileName must be String')
        # load file
        fileJson ={}
        try:
            file = open(fileName,'r')
        except Exception as err:
            print('file = open(fileName,\'r\'\n', err)
            return
        fileJson['name'] = file.name
        fileJson['content'] = file.read()
        file.close()
        msg = json.dumps(fileJson)
        
        #accept connections
        try:
            self.c, cAdr = self.s.accept()
            print('Got connection from\n', cAdr)
        except Exception as err:
            print('self.c, cAdr = self.s.accept()',err)
            return

        #send file
        self.c.send(msg.encode())

    def send(self, msg):
        try:
            self.c.send(msg)
        except Exception as err:
            print('self.s.send(msg)\n',err)

    def close_server(self):
        try:
            self.s.close()
        except Exception as err:
            print('self.s.close()',err)
            return
    def close_connection(self):
        try:
            self.c.close()
        except Exception as err:
            print('self.s.close()',err)
    
        
