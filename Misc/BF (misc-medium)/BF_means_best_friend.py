import socketserver
import time
import threading
import string
import random
import hashlib

class Service(socketserver.BaseRequestHandler):
    def handle(self):
        
        string_len = 12
        
        
        f = open('flags.txt', 'r')
        
        random_string = random.choices(string.ascii_letters + string.digits, k=string_len)
        
        answer = ""
        for i in range (4):
            random_hidden_location = random.randint(0, string_len - 1)
            while random_string[random_hidden_location] == '*':
                random_hidden_location = random.randint(0, string_len - 1)
            answer += random_string[random_hidden_location]
            random_string[random_hidden_location] = '*'
            
        
        hash_ans = hashlib.md5(answer.encode()).hexdigest()


        #self.send(answer)
        self.send("".join(random_string) + " ->  " + hash_ans)
        self.send('(string -> hash md5)\n')
        self.send('Find the hidden characters in the string above! Hidden character are the "*".')
        self.send('Enter the hidden characters in the correct order.')
        
        
    
        #self.send('XXXX ->  ' + hash_ans)
        
        usr_input = self.recieve().decode()
        
        if usr_input == answer:
            self.send('Correct!')
            self.send('Your flag is: ' + f.read())
        else:
            self.send('Incorrect!')
        
        
    
    def send(self, string, newline=True):
        if newline:
            string += '\n'
            self.request.sendall(string.encode())
            
    def recieve(self, prompt='> '):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()

class ThreadedService(socketserver.ThreadingMixIn, socketserver.TCPServer, socketserver.DatagramRequestHandler):
    
    pass
    

def main():
    port = 5664
    host = '0.0.0.0'
    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print('Server started on {}:{}'.format(host, port))
    
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
    