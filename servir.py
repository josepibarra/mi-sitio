"""Vista previa local: python3 servir.py  ->  http://localhost:8000"""
import http.server, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sitio')
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=RAIZ, **k)
    def send_error(s, code, message=None, explain=None):
        p = os.path.join(RAIZ, '404.html')
        if code == 404 and os.path.exists(p):
            b = open(p, 'rb').read(); s.send_response(404); s.send_header('Content-Type', 'text/html; charset=utf-8'); s.send_header('Content-Length', str(len(b))); s.end_headers(); s.wfile.write(b)
        else: super().send_error(code, message, explain)
print('NODO v5 en http://localhost:8000  (Ctrl+C para salir)')
http.server.ThreadingHTTPServer(('127.0.0.1', 8000), H).serve_forever()
