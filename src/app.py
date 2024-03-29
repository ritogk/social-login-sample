from flask import Flask
from routes.api import api
from routes.view import view
import db.models.all
import db.db as db
# webアプリケーション作成


def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)
    # db関係の設定
    db.init_db(app)
    db.init_seeder(app)
    # ルーティングの設定
    app.register_blueprint(view)
    app.register_blueprint(api)

    return app


# app = create_app()
