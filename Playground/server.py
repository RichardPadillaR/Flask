from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<number_of_boxes>')
def number_boxes(number_of_boxes):
    repeat = int(number_of_boxes)
    return render_template('boxes.html', repeat = repeat)

@app.route("/play/<number_of_boxes>/<color_change>")
def box_color(number_of_boxes,color_change):
    repeat = (int(number_of_boxes))
    colorChange = color_change
    return render_template('color.html', repeat = repeat, colorChange = colorChange )

if __name__=="__main__":   
    app.run(debug=True, port = 5100)