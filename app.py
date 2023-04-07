from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global guesses
    global max_guesses
    key=[]
    key.append(int(request.form['guessed_array1']))
    key.append(int(request.form['guessed_array2']))
    key.append(int(request.form['guessed_array3']))
    key.append(int(request.form['guessed_array4']))

    signal=[]
    signal.append(float(request.form['guessed_signal1']))
    signal.append(float(request.form['guessed_signal2']))
    signal.append(float(request.form['guessed_signal3']))
    signal.append(float(request.form['guessed_signal4']))
    signal.append(float(request.form['guessed_signal5']))
    signal.append(float(request.form['guessed_signal6']))
    signal.append(float(request.form['guessed_signal7']))
    signal.append(float(request.form['guessed_signal8']))
    signal.append(float(request.form['guessed_signal9']))
    signal.append(float(request.form['guessed_signal10']))
    signal.append(float(request.form['guessed_signal11']))
    signal.append(float(request.form['guessed_signal12']))
    

    # coordinates.py file
    coords = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    c = 0
    j=0 
    for i in range(len(key)):
        inv = (key[i] + 1)**2
        coords[j][c%2] = round(signal[i]*inv)
        c+=1
        if(c%2==0 and c!=0):
            j+=1

    for i in range(len(key)):
        inv = (key[i] + 2)**1.5
        coords[j][c%2] = round(signal[i+4]*inv)
        c+=1
        if(c%2==0 and c!=0):
            j+=1

    for i in range(len(key)):
        inv = (key[i] + 3)**3
        coords[j][c%2] = round(signal[i+8]*inv)
        c+=1
        if(c%2==0 and c!=0):
            j+=1

    #end of co-ordinates.py file
    
    return render_template('index.html', message=coords)

if __name__ == '__main__':
    app.run(debug=True)
