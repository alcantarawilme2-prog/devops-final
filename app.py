from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Final</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 50px 60px;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
        }
        .emoji { font-size: 60px; margin-bottom: 20px; }
        h1 { color: #333; font-size: 2.5em; margin-bottom: 10px; }
        p { color: #666; font-size: 1.1em; margin-bottom: 30px; }
        .badges { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
        .badge {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
        }
        .footer { margin-top: 30px; color: #999; font-size: 0.85em; }
    </style>
</head>
<body>
    <div class="card">
        <div class="emoji">🚀</div>
        <h1>Hola Mundo!</h1>
        <p>Aplicacion desplegada con el pipeline CI/CD completo</p>
        <div class="badges">
            <span class="badge">Python Flask</span>
            <span class="badge">Docker</span>
            <span class="badge">GitHub Actions</span>
            <span class="badge">Render</span>
        </div>
        <div class="footer">DevOps Final — Alcantara Wilme</div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)