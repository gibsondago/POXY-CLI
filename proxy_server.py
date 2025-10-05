"""
Proxy Manager CLI - Proxy Server

Author: Rezaul Karim
Email: work.rezaul@outlook.com
Powered By: REZ LAB

Implements local proxy server functionality that forwards to upstream proxy.
"""

import socket
import threading
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import socks
import select

class HTTPProxyHandler(BaseHTTPRequestHandler):
    def do_CONNECT(self):
        """Handle CONNECT request for HTTPS connections"""
        try:
            # Establish connection to upstream proxy
            upstream_host = self.server.upstream_host
            upstream_port = self.server.upstream_port
            
            # Create socket to upstream proxy
            upstream_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            upstream_sock.connect((upstream_host, int(upstream_port)))
            
            # Send CONNECT request to upstream proxy
            connect_request = f"CONNECT {self.path} HTTP/1.1\r\nHost: {self.path}\r\n\r\n"
            upstream_sock.send(connect_request.encode())
            
            # Receive response from upstream proxy
            response = upstream_sock.recv(4096)
            if b"200 Connection established" in response:
                # Send successful response to client
                self.send_response(200, "Connection established")
                self.end_headers()
                
                # Start forwarding data between client and upstream proxy
                self._forward_data(self.connection, upstream_sock)
            else:
                self.send_error(502, "Upstream proxy connection failed")
        except Exception as e:
            self.send_error(500, f"Error: {str(e)}")
    
    def do_GET(self):
        """Handle GET request through upstream proxy"""
        try:
            upstream_host = self.server.upstream_host
            upstream_port = self.server.upstream_port
            
            # Create socket to upstream proxy
            upstream_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            upstream_sock.connect((upstream_host, int(upstream_port)))
            
            # Prepare request to send to upstream proxy
            request = f"GET {self.path} HTTP/1.1\r\nHost: {self.headers['Host']}\r\n"
            for header in self.headers:
                if header.lower() not in ['connection', 'proxy-connection']:
                    request += f"{header}: {self.headers[header]}\r\n"
            request += "Connection: close\r\n\r\n"
            
            # Send request to upstream proxy
            upstream_sock.send(request.encode())
            
            # Receive response from upstream proxy
            response = upstream_sock.recv(4096)
            
            # Parse response to get status line
            response_str = response.decode('utf-8', errors='ignore')
            status_line = response_str.split('\r\n')[0]
            status_code = int(status_line.split()[1])
            
            # Send response to client
            self.send_response(status_code)
            
            # Forward headers
            for line in response_str.split('\r\n')[1:]:
                if line:
                    header_parts = line.split(':', 1)
                    if len(header_parts) == 2:
                        self.send_header(header_parts[0], header_parts[1].strip())
                else:
                    break
            
            self.end_headers()
            
            # Send body response
            body_start = response_str.find('\r\n\r\n') + 4
            if body_start > 3:  # If we found the body
                self.wfile.write(response[body_start:])
            
            # Forward remaining data
            while True:
                more_data = upstream_sock.recv(4096)
                if not more_data:
                    break
                self.wfile.write(more_data)
                
        except Exception as e:
            self.send_error(500, f"Error: {str(e)}")
    
    def _forward_data(self, client_sock, upstream_sock):
        """Forward data between client and upstream proxy"""
        try:
            while True:
                # Use select to handle data in both directions
                ready, _, _ = select.select([client_sock, upstream_sock], [], [], 1)
                
                if client_sock in ready:
                    data = client_sock.recv(4096)
                    if not data:
                        break
                    upstream_sock.send(data)
                
                if upstream_sock in ready:
                    data = upstream_sock.recv(4096)
                    if not data:
                        break
                    client_sock.send(data)
        except Exception:
            pass  # Connection closed
        finally:
            client_sock.close()
            upstream_sock.close()

# Global list to keep track of running servers for proper shutdown
running_servers = []

def start_http_proxy(local_port, upstream_host, upstream_port):
    class Proxy(HTTPServer):
        def __init__(self, server_address, handler_class):
            super().__init__(server_address, handler_class)
            self.upstream_host = upstream_host
            self.upstream_port = upstream_port
    
    server = Proxy(('localhost', local_port), HTTPProxyHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    
    # Add to running servers list for potential cleanup
    running_servers.append(server)
    
    return server

def stop_all_servers():
    """Stop all running proxy servers"""
    for server in running_servers:
        try:
            server.shutdown()
            server.server_close()
        except Exception as e:
            print(f"Error stopping server: {e}")
    
    # Clear the list
    running_servers.clear()

def start_socks_proxy(local_port, upstream_host, upstream_port, username=None, password=None):
    """Start a SOCKS proxy server that forwards to upstream proxy"""
    import socketserver
    
    class SocksProxyHandler(socketserver.BaseRequestHandler):
        def handle(self):
            # This is a simplified SOCKS proxy implementation
            # For a fully functional SOCKS proxy, a more complex implementation is needed
            upstream_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            upstream_sock.connect((upstream_host, int(upstream_port)))
            
            # Forward data between client and upstream proxy
            try:
                while True:
                    ready, _, _ = select.select([self.request, upstream_sock], [], [], 1)
                    
                    if self.request in ready:
                        data = self.request.recv(4096)
                        if not data:
                            break
                        upstream_sock.send(data)
                    
                    if upstream_sock in ready:
                        data = upstream_sock.recv(4096)
                        if not data:
                            break
                        self.request.send(data)
            except Exception:
                pass  # Connection closed
            finally:
                self.request.close()
                upstream_sock.close()
    
    server = socketserver.TCPServer(('localhost', local_port), SocksProxyHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    
    # Add to running servers list for potential cleanup
    running_servers.append(server)
    
    return server