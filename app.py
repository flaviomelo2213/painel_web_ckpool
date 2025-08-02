from flask import Flask, render_template_string
import os
app = Flask(__name__)

@app.route('/')
def index():
 log_path = os.path.expanduser('~/ckpool_merge_solo/ckpool.log')
 lines = open(log_path).readlines()[-30:] if os.path.exists(log_path) else ['Log não encontrado']
 return render_template_string('<pre>{{log}}</pre>', log=''.join(lines))

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
