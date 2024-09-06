from flask import Flask, request, render_template_string
import telebot


app = Flask(__name__)


def notifyMe(name, message):
    print(name, message)


@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')

    notifyMe(name, message)

    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recruto</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Hello {{ name }}!</h1>
        <p>{{ message }}</p>
    </body>
    <footer>
    
    </footer>
    </html>
    """

    return render_template_string(html_template, name=name, message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)