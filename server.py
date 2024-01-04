from flask import Flask, render_template, request
from sg_ccentric import check_code_c_centric
from waitress import serve
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/ccentric')
def get_code():
    imei = request.args.get('imei' ,'')
    result_code_c_centric = check_code_c_centric(imei)
    #print(imei)
    #print(result_code_c_centric)
    
    return render_template(
        "ccentric.html",
        imei=imei,  # Pass imei to the template
        result = result_code_c_centric
    )

if __name__== "__main__":
    serve(app, host="0.0.0.0",port=8000)
