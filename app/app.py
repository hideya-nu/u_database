# Flaskとrender_template（HTMLを表示させるための関数）をインポート
# ライブラリにrequestもインポート
from flask import Flask,render_template,request
from models.models import MotimonoContent
from models.database import db_session

# Flaskオブジェクトの生成
app = Flask(__name__)


# /へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


# /indexへアクセスがあった場合に、index.htmlを返す
@app.route("/index")
def index():
    name = request.args.get("name") #クエリストリングからname属性の値を受け取る
    all_motimono = MotimonoContent.query.all()
    return render_template("index.html",name=name,all_motimono=all_motimono)

    # list = ["筆箱","交通IC","携帯","自転車の鍵","家の鍵","パソコン"] #listに持ち物リストを定義
    # return render_template("index.html",name=name,list=list) #index.htmlにnameの情報を送ってwebページを表示させる

# /indexにPOSTリクエストがあった場合に、フォームのテキスト要素を取得し、nameとしてhtml側に値を渡す
@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    all_motimono = MotimonoContent.query.all()
    return render_template("index.html", name=name, all_motimono=all_motimono)

    # list = ["筆箱","交通IC","携帯","自転車の鍵","家の鍵","パソコン"]
    # return render_template("index.html",name=name,list=list)

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = MotimonoContent(title,body)
    db_session.add(content)
    db_session.commit()
    return index()

@app.route("/update",methods=["post"])
def update():
    content = MotimonoContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = MotimonoContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

# app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)