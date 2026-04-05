from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'students.csv')
    df = pd.read_csv(csv_path)

    df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

    topper = df.loc[df["Average"].idxmax()]
    weak_students = df[df["Average"] < 50]

    return render_template(
        "index.html",
        tables=[df.to_html(classes='data', index=False)],
        topper=topper["Name"],
        weak=[weak_students.to_html(classes='data', index=False)]
    )

if __name__ == '__main__':
    app.run(debug=True)
