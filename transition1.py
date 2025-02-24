from flask import Flask,render_template,session,redirect,request
import os

app = Flask(__name__, static_folder="./static/")
# セッションを使うための初期値を与える
app.secret_key = os.urandom(24)

# ログインチェックしないパターン

@app.route('/')
def loginform():
    # セッションデータに値を格納
    # session['test'] = 'セッションにテストデータ格納'
    # 01login.htmlでセッションを利用している
    return render_template('transition/01login.html')

# formのポストでログイン処理する
@app.route('/confirm',methods=["POST"])
def confirm():
    name = "jeff"
    # name = request.form.get('name')
    # トップページを表示する
    return render_template('transition/01toppage.html', name=name)

@app.route('/link1')
def link1():
    return render_template('transition/01link1.html')

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=False)