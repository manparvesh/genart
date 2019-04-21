from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def spriteGenerator():
    size = int(request.args.get('size'))
    invaders = int(request.args.get('invaders'))
    imageSize = int(request.args.get('imageSize'))

    from spritegenerator import spriteGenerator
    return spriteGenerator(size, invaders, imageSize)


@app.route('/')
def homepage():
    size = 7
    invaders = 5
    imageSize = 1000

    if request.args.get('size') is not None:
        size = int(request.args.get('size'))

    if request.args.get('invaders') is not None:
        invaders = int(request.args.get('invaders'))

    if request.args.get('imageSize') is not None:
        imageSize = int(request.args.get('imageSize'))

    return """
    <p>
    The default values being used are:
    <br>
    size = 7
    invaders = 55
    imageSize = 1000
    <br>
    To change the values, use it like this: /?imageSize=1900&invaders=30
    </p>

    <img src="/api?size={size}&invaders={invaders}&imageSize={imageSize}" />
    """.format(size=size, invaders=invaders, imageSize=imageSize)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
