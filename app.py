from flask import Flask, render_template, request
app = Flask(__name__)

from model import DataManager

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/managedata")
def ManageData():
	return render_template('datamanager.html')

@app.route("/displaydata")
def ViewData():
	df = DataManager.getDataToDisplay()
	df_html = df.to_html()
	return render_template('dataviewer.html', table_html=df_html)

if __name__ == "__main__":
  app.run()