#!/usr/bin/env python3

"""Servidor web mínimo y robusto para entorno local/contenedor."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        if self.path in ("/", "/index.html"):
            self.path = "/index.html"
            return super().do_GET()
        self.send_error(404, "No encontrado")


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"✅ Servidor activo en http://{HOST}:{PORT}")
    print("Si estás en tu máquina, abre: http://127.0.0.1:8000")
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
