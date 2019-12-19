from flask import Flask, render_template

  
app = Flask(__name__) 





@app.route('/')
def index(): 
   return render_template('index.html')
	

@app.route('/networkpenetration')
def networkpenetration():
   return render_template('networkpenetration.html')
	
	


@app.route('/pythonprogramming')
def pythonprogramming():
   return render_template('pythonprogramming.html')
	
	
   
@app.route('/mobilepenetration')
def mobilepenetration():
   return render_template('mobilepenetration.html')
	
@app.route('/diplomainpenetration')
def diplomainpenetration():
   return render_template('diplomainpenetration.html')
	
      
@app.route('/ethicalhacking')
def ethicalhacking():
   return render_template('ethicalhacking.html')
   
@app.route('/diplomaincybersecurity')
def diplomaincybersecurity():
   return render_template('diplomaincybersecurity.html')



@app.route('/informationsecurityservices')
def informationsecurityservices():
   return render_template('informationsecurityservices.html')


@app.route('/about')
def about():
   return render_template('about.html')
	
@app.route('/webpenetration')
def webpenetration():
   return render_template('webpenetration.html')
	
@app.route('/workshopseminars')
def workshopseminars():
   return render_template('workshopseminars.html')
	

   

@app.route('/ceh')
def ceh():
   return render_template('ceh.html')
	

@app.route('/contact')
def contact():
   return render_template('contact.html')
	

@app.route('/testimonials')
def testimonials():
   return render_template('testimonials.html')
	

   
@app.route('/service')
def service():
   return render_template('service.html')
	


@app.route('/courses')
def courses():
   return render_template('courses.html')
	

@app.route('/corporatetraining')
def corporatetraining():
   return render_template('corporatetraining.html')
	
@app.route('/cyberforensics')
def cyberforensics():
   return render_template('cyberforensics.html')
	

	
if __name__ == '__main__':
   app.run(port=5001,debug=True) 
   