# Temel imaj (Python 3.9)
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Modeli ve uygulama kodunu kopyala
COPY heart_disease_model.pkl .
COPY app.py .

# Uygulamayı çalıştır
CMD ["python", "app.py"]