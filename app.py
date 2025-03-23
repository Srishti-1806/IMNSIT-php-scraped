import pandas as pd
from flask import Flask



app = Flask(__name__)
with open("output.html","w")as file:
    
    @app.route('/')
    def index():
        a = pd.read_csv(r'C:\Users\DINESH KUMAR\Desktop\imnsit\data.csv')
        html_df = a.to_html()
        file.write(html_df)
        return html_df 
    if __name__ == '__main__':
        app.run(debug=True)


