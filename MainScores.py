
from flask import Flask
import Utils


app = Flask(__name__)

@app.route("/")
def score_server():
    with open(Utils.SCORES_FILE_NAME, 'r') as file:
        current_score = file.read()
        SCORE= current_score
        ERROR= Utils.BAD_RETURN_CODE
    if current_score.isdigit():
        html_success_message = '''
             <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{SCORE}</div></h1>
                </body>
            </html>'''.format(SCORE=SCORE)
        return html_success_message

    else:
        html_error_message = '''
            <html>
                <head>
                    <title>Score Game</title>
                </head>
                <body>
                    <div id="score" style="color:red">{ERROR}</div>
                </body>
            </html>'''
        return html_error_message
app.run('0.0.0.0')

score_server()