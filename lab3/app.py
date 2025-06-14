from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return "Файл не загружен", 400

        try:
            data = pd.read_csv(file, on_bad_lines='skip', low_memory=False)
        except Exception as e:
            return f"Ошибка при чтении CSV: {str(e)}", 400

        numeric_data = data.select_dtypes(include=['number'])

        if numeric_data.shape[1] < 2:
            preview_html = data.head().to_html()
            return render_template('result.html', preview=preview_html, img_data=None)

        X = numeric_data.iloc[:, :-1]
        y = numeric_data.iloc[:, -1]

        if X.isnull().any().any() or y.isnull().any():
            return "Данные содержат пропущенные значения", 400

        try:
            model = LinearRegression().fit(X, y)
            y_pred = model.predict(X)
        except Exception as e:
            return f"Ошибка при обучении модели: {str(e)}", 500

        plt.figure(figsize=(8, 5))
        plt.plot(y.values, label='Real')
        plt.plot(y_pred, label='Predicted')
        plt.legend()
        plt.title('Реальные vs Предсказанные')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode()
        plt.close()

        return render_template('result.html', img_data=img_base64, preview=None)

    return render_template('index.html')
