from crypt import methods
from flask import Flask, redirect, render_template, Request, request, url_for #render_template for html files, request: for POST OR GET Request

app = Flask(__name__)

todoData = []

@app.route("/")
def index():
    return render_template("index.html", todos = todoData) #Once the function is called, it return the html file 'index.html'
    
@app.route('/create-todo', methods = ['POST'])
def create_todo():
    new_todo = request.form.get("new_todo")
    # return new_todo # this print a request from the form
    todoData.append(new_todo)
    print(todoData)
    
    return redirect(url_for("index")) #This line redirect you to index page     

@app.route('/delete/<todo_item>')
def delete(todo_item):
    todoData.remove(todo_item)
        
    return redirect(url_for('index'))

index_to_update = ""

@app.route('/update/<todo_item>', methods = ['GET', 'POST'])
def update(todo_item):
    
    index = todoData.index(todo_item)
    
    global index_to_update
    index_to_update = index 
    
    return render_template('update.html', todo_item = todo_item)

@app.route('/update_item', methods = ['POST'])
def update_item():
       
    if request.form == 'POST':
        new_item = request.form.get('new_item')
        
        todoData[index_to_update] = new_item
        return redirect(url_for('index'))
    else:
        return "<h3 style = 'color:red;'>Error: No Updates!</h3>"

if __name__== "__main__":
    app.run(debug=True)