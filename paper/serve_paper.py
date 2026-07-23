import http.server
import socketserver
import urllib.parse
import json
import os
import subprocess

PORT = 8008
PAPER_TEX = "/home/charizard/computational-coupling/paper/main.tex"
PDF_OUT = "/home/charizard/computational-coupling/paper/output/paper.pdf"
COMPILER_SCRIPT = "/home/charizard/computational-coupling/paper/compile_paper.py"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Local Overleaf Editor — Theory of Computational Coupling</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; height: 100vh; background: #1e1e1e; color: #d4d4d4; }
        #sidebar { width: 50%; height: 100%; display: flex; flex-direction: column; border-right: 2px solid #333; }
        #toolbar { padding: 10px 16px; background: #252526; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; }
        #toolbar h2 { font-size: 14px; color: #61afef; font-weight: 600; }
        .btn { background: #2e75b6; color: #fff; border: none; padding: 6px 14px; border-radius: 4px; font-size: 12px; font-weight: bold; cursor: pointer; }
        .btn:hover { background: #1f4e78; }
        #editor { flex: 1; width: 100%; padding: 16px; background: #1e1e1e; color: #9cdcfe; font-family: "Courier New", monospace; font-size: 13px; line-height: 1.5; border: none; resize: none; outline: none; }
        #preview { width: 50%; height: 100%; background: #525659; }
        iframe { width: 100%; height: 100%; border: none; }
        #status { font-size: 11px; color: #98c379; }
    </style>
</head>
<body>
    <div id="sidebar">
        <div id="toolbar">
            <h2>📄 paper/main.tex (Local Overleaf Editor)</h2>
            <div>
                <span id="status">Ready</span> &nbsp;
                <button class="btn" onclick="saveAndCompile()">Recompile (Ctrl+S)</button>
            </div>
        </div>
        <textarea id="editor" spellcheck="false">__TEX_CONTENT__</textarea>
    </div>
    <div id="preview">
        <iframe id="pdfFrame" src="/pdf"></iframe>
    </div>

    <script>
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                saveAndCompile();
            }
        });

        function saveAndCompile() {
            document.getElementById('status').innerText = "Compiling...";
            const content = document.getElementById('editor').value;
            fetch('/save', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ content: content })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('status').innerText = "Compiled successfully!";
                document.getElementById('pdfFrame').src = "/pdf?t=" + new Date().getTime();
            })
            .catch(err => {
                document.getElementById('status').innerText = "Error compiling!";
            });
        }
    </script>
</body>
</html>
"""

class LocalOverleafHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            with open(PAPER_TEX, 'r', encoding='utf-8') as f:
                tex_content = f.read()
            html = HTML_TEMPLATE.replace('__TEX_CONTENT__', tex_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path.startswith('/pdf'):
            if os.path.exists(PDF_OUT):
                with open(PDF_OUT, 'rb') as f:
                    pdf_bytes = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/pdf')
                self.send_header('Content-Length', str(len(pdf_bytes)))
                self.end_headers()
                self.wfile.write(pdf_bytes)
            else:
                self.send_error(404, "PDF not found")
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(length).decode('utf-8'))
            with open(PAPER_TEX, 'w', encoding='utf-8') as f:
                f.write(data['content'])
            subprocess.run(["python3", COMPILER_SCRIPT], check=True)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode('utf-8'))

def serve():
    with socketserver.TCPServer(("", PORT), LocalOverleafHandler) as httpd:
        print(f"Local Overleaf Server running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    serve()
