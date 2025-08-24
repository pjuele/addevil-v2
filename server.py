#!/usr/bin/env python3
"""
Simple HTTP server for ADDevil project
Run with: python server.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

def main():
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 ADDevil server running at http://localhost:{PORT}")
            print(f"📁 Serving files from: {os.getcwd()}")
            print(f"🎯 Open wireframes at: http://localhost:{PORT}/wireframes.html")
            print("Press Ctrl+C to stop")
            
            # Auto-open browser
            webbrowser.open(f'http://localhost:{PORT}/wireframes.html')
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Try a different port or kill the existing process.")
            sys.exit(1)
        else:
            raise

if __name__ == "__main__":
    main()