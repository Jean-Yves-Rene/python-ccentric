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
    # Check if the IMEI is a numeric value and has a length of 15
    if imei.isdigit() and len(imei) == 15:
        result_code_c_centric = check_code_c_centric(imei)
        #print(imei)
        #print(result_code_c_centric)
        return render_template(
            "ccentric.html",
            imei=imei,  # Pass imei to the template
            result = result_code_c_centric
        )
    else:
        return render_template("invalid_imei.html")
if __name__== "__main__":
    serve(app, host="0.0.0.0",port=8000)
