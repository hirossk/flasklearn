from flask import Flask,render_template,session,redirect
import os

app = Flask(__name__, static_folder="./static/")
# セッションを使うための初期値を与える
app.secret_key = os.urandom(24)

# ログインチェック有りのパターン

# ログイン状態を確認するための関数[flask_login]を使う方法は機能が多い
def login_check():
    if (session.get('logoned') == True):
        return True
    else:
        return False

@app.route('/')
def loginform():
    # セッションデータに値を格納
    session['test'] = 'セッションにテストデータ格納'
    # 01login.htmlでセッションを利用している
    return render_template('transition/01login.html')

# formのポストでログイン処理する
@app.route('/confirm',methods=["POST"])
def confirm():
    # パスワードチェックしていないため必ずログインできる
    # request.args.get('key')はGETメソッドの時
    # request.form.get('key')はPOSTメソッドの時
    # 本当はパスワードチェックすべき
    session['logoned'] = True
    # トップページを表示する
    return render_template('transition/01toppage.html')

@app.route('/logout')
def logout():
    # ログアウト（セッションデータ更新）後'/'にリダイレクトする
    session['logoned'] = False
    return redirect("/")
    
@app.route('/toppage')
def toppage():
    # ログインで来ていなければ'/'にリダイレクトする
    if(login_check() == True):
        return render_template('transition/01toppage.html')
    else:
        return redirect("/")

@app.route('/link1')
def link1():
    # ログインで来ていなければ'/'にリダイレクトする
    if(login_check() == True):
        return render_template('transition/01link1.html')
    else:
        return redirect("/")

@app.route('/link2')
def link2():
    # ログインで来ていなければ'/'にリダイレクトする
    if(login_check() == True):
        # 辞書データに格納する
        send_data = {
            'key1' : 999,
            'key2' : 'Moji',
            'key3' : '2024-2-29'
        }
        # 辞書データに格納した値をhtml内で利用する
        return render_template('transition/01link2.html',data = send_data)
    else:
        return redirect("/")

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=False)