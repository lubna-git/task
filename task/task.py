
from flask import Flask, app, render_template,request
from math import sqrt,pi,exp

from werkzeug.utils import redirect
app = Flask(__name__)

# the male parametar
hieght1 = [6,5.92,5.58,5.92]
weight1 = [180,190,170,165]
foot_size1 = [12,11,12,10]
man=[hieght1,weight1,foot_size1]
# the female parameter
hieght2 = [5,5.5,5.42,5.75]
weight2 = [100,150,130,150]
foot_size2 = [6,8,7,9]
woman = [hieght2,weight2,foot_size2]
person = [man,woman]



def mean_f(x):
    lenght = len(x)
    
    total_sum = 0
    for i in range(lenght):
        total_sum += x[i]
        total_sum = sum(x)
        avg = total_sum/lenght
    return avg

def variance_f(x):
    lenght = len(x)
    total_sum1 = 0
    for i in range(lenght):
        sub = pow(x[i]-mean_f(x), 2)
        total_sum1 +=sub
        var = total_sum1/(lenght-1)
    return  var


@app.route('/', methods=["POST","GET"])
def person_f():
    if request.method == "POST":
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        foot_size = request.form['foot_size']
    
        m = [height,weight,foot_size]
        for x in m:
            try:
                x = float(x)
                try:
                    name == float(name)
                    return render_template("task.html",error='*Please enter number  in the following fields except  the Full Name field.')
                except:
                    continue
            except ValueError:
                return render_template("task.html",error='*Please enter number  in the following fields except  the Full Name field.')
                
               
        mean_male = []
        mean_female =[]
        variance_male = []
        variance_female = []
        probability_m = []
        probability_f = []
        male = 0
        female = 1
        for x in  person[male]:
            mean_male.append(mean_f(x))
            variance_male.append(variance_f(x))
        for x in person[female]:
            mean_female.append(mean_f(x))
            variance_female.append(variance_f(x))
        i = 0
        for x in m:
            p_male= (1/sqrt(2*pi*variance_male[i]))*exp(-1*pow(float(x)-mean_male[i],2)/(2*variance_male[i]))
            probability_m.append(p_male)
            p_female=(1/sqrt(2*pi*variance_female[i]))*exp(-1*pow(float(x)-mean_female[i],2)/(2*variance_female[i]))
            probability_f.append(p_female)
            i +=1
        lenght = len(probability_m)
        total1_sum = 1
        for i in range(lenght):
            total1_sum = total1_sum*probability_m[i]
            probability_male = 0.5*total1_sum
        total1_sum = 1
        for i in range(lenght):
            total1_sum = total1_sum*probability_f[i]
            probability_female= 0.5*total1_sum
        if probability_male<probability_female:
            gender = "female"
        else:
            gender = "male"
        

        return render_template("result.html",gender=gender, name=name)
    else:
        return render_template("task.html", error='')

            
            
if __name__ == '__main__':
    app.run(debug=True)


          

        

                