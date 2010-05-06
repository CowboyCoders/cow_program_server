import sys
import BaseHTTPServer
import shutil
import os.path
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

def main():
    if len(sys.argv[1:]) != 3:
        print "Usage: program_table_server <ip> <port> <program-table-file>"
        sys.exit(2)
    else:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        file = sys.argv[3]
        if file != "program_table.xml":
            try:
                shutil.copyfile(file,"program_table.xml")
            except IOError, err:
                print "Could not copy program_table.xml to server root. Please check the filename!"
                sys.exit(2)
        else:
            if not os.path.isfile("program_table.xml"):
                print "Could not find program_table.xml in this folder. Please check the filename!"
                sys.exit(2)
        server_adress = (ip,port)
        HandlerClass.protocol_version = Protocol
        httpd = ServerClass(server_adress,HandlerClass)

        sa = httpd.socket.getsockname()
        print "Running program_table server on ", sa[0], " port ", sa[1], "..."
        httpd.serve_forever()

if __name__ == "__main__":
    main()
