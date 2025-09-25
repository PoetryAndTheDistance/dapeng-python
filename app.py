from flask import Flask, request
from bao_stack.api import bao_stack


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 注册所有API蓝图
app.register_blueprint(bao_stack)


if __name__ == '__main__':
    app.run()
