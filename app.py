from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 서버 삭제 

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def recipe_post():
    food_receive = request.form["food_give"]
    recipe_receive = request.form["recipe_give"]

    doc = {
        'food': food_receive,
        'recipe': recipe_receive
    }

    db.recipes.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

# #삭제 미구현
# @app.route("/homework", methods=["DELETE"])
# def recipe_del():
#     food_receive = request.form["food_give"]
#
#     return jsonify({'msg':'삭제 완료!'})

@app.route("/homework", methods=["GET"])
def recipe_get():
    recipe_list = list(db.recipes.find({},{'_id':False}))
    return jsonify({'recipes': recipe_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)