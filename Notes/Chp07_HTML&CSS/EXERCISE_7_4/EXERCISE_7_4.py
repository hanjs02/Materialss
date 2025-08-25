from flask import Flask, render_template 

app = Flask(__name__)

def school_population(): 
    population = []
    with open('people.txt', 'r') as f: 
        for line in f: 
            line = line.strip()
            if line == '': 
                continue 
            name, dob, identity = line.split(',')
            year, month, day = dob.split('-')
            clean_name = name.replace(' ', '')
            screen_name = clean_name + month + day

            population.append({
                'full_name': name,
                'screen_name': screen_name,
                'identity': identity 
            })
    return population

@app.route('/')
def index(): 
    population = school_population()
    return render_template('index.html', population=population)

if __name__ == '__main__': 
    app.run(debug=True)
    


