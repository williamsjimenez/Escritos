#!/usr/bin/env python3

"""Servidor web mínimo para ver el proyecto en navegador."""

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        if self.path not in ("/", "/index.html"):
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("No encontrado".encode("utf-8"))
            return

        html = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Escritos - OK</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }
    main { min-height: 100vh; display: grid; place-items: center; padding: 24px; }
    .card { max-width: 680px; width: 100%; background: #111827; border: 1px solid #334155; border-radius: 14px; padding: 24px; }
    h1 { margin-top: 0; }
    code { background: #1f2937; padding: 2px 6px; border-radius: 6px; }
  </style>
</head>
<body>
  <main>
    <section class="card">
      <h1>✅ ¡Ya está funcionando!</h1>
      <p>Tu proyecto ya se está ejecutando como aplicación web local.</p>
      <p>URL activa: <code>http://127.0.0.1:8000</code></p>
    </section>
  </main>
</body>
</html>
"""

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


def main() -> None:
    server = HTTPServer((HOST, PORT), Handler)
    print(f"✅ Servidor activo en http://{HOST}:{PORT}")
    print("Presiona Ctrl + C para detenerlo.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("Servidor detenido.")


if __name__ == "__main__":
    main()
