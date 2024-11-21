from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data/headlines.json', 'r') as file:
        headlines = json.load(file)
    return render_template('index.html', documents=headlines)

@app.route('/document/<int:doc_id>')
def document(doc_id):
    with open('data/headlines.json', 'r') as file:
        headlines = json.load(file)
    if doc_id < 0 or doc_id >= len(headlines):
        return "Invalid document ID"

    selected_document = headlines[doc_id]
    return render_template('document.html', document=selected_document)

@app.route('/categories')
def categories():    
    with open('data/category_details.json', 'r') as file:
        category_details = json.load(file)
        
    print(category_details)

    return render_template('categories.html', category_details=category_details)

@app.route('/category/<category_name>')
def category_detail(category_name):
    with open('data/category_details.json', 'r') as file:
        category_details = json.load(file)
        
    with open('data/headlines.json', 'r') as file:
        headlines = json.load(file)

    # Find the selected category
    selected_category = next((cat for cat in category_details if cat['category_name'] == category_name), None)

    if not selected_category:
        return "Category not found"

    return render_template('category_detail.html', category=selected_category, headlines=headlines)

@app.route('/clusters')
def clusters():
    with open('data/cluster_details.json', 'r') as file:
        cluster_details = json.load(file)
        
    return render_template('clusters.html', cluster_details=cluster_details)

@app.route('/cluster/<int:cluster_index>')
def cluster_detail(cluster_index):
    with open('data/cluster_details.json', 'r') as file:
        cluster_details = json.load(file)
        
    with open('data/headlines.json', 'r') as file:
        headlines = json.load(file)

    # Find the selected cluster
    selected_cluster = next((cluster for cluster in cluster_details if cluster['cluster_index'] == cluster_index), None)

    if not selected_cluster:
        return "Cluster not found"

    return render_template('cluster_detail.html', cluster=selected_cluster, headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)