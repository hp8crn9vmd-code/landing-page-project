#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys
from pathlib import Path

def run_preview_server(port=8080):
    project_dir = Path(__file__).parent.parent
    os.chdir(project_dir)
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Serving from: {project_dir}")
            print(f"Preview URL: http://localhost:{port}")
            print("Press Ctrl+C to stop.")
            httpd.serve_forever()
    except OSError:
        print(f"Port {port} is busy. Try: python tools/preview.py --port 8081")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Server stopped.")
        sys.exit(0)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Preview landing page")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port number")
    args = parser.parse_args()
    run_preview_server(args.port)