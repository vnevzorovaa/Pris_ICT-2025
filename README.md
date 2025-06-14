# Pris_ICT-2025

# 1. Minikube 

## Предварительные требования

- Установлен [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- Установлен [kubectl](https://kubernetes.io/docs/tasks/tools/)
- Установлен [Docker](https://docs.docker.com/get-docker/)
- Установлен [Helm](https://helm.sh/docs/intro/install/)
- Включен режим `minikube start --driver=docker`

## Запуск

### Запускаем Minikube

```bash
minikube start --driver=docker
```
### Сборка образа 
```bash
docker build -t my-app:latest .
```
### Применение манифестов 
```bash
kubectl apply -f <file-name.yaml>
```
### Установка Metrics Server
```bash
helm install metrics-server metrics-server/metrics-server --namespace kube-system
```
### HPA 
```bash
kubectl autoscale deployment my-app --cpu-percent=50 --min=2 --max=5
```
### Просмотр логов в stdout
```bash
kubectl logs app -f -n <namespace-name>
```
### Вывод всех подов 
```bash 
kubectl get pods -A
```
### Доступ к графане 
```bash
kubectl port-forward svc/prometheus-grafana 3000:80
```

# 1. GraphQL

## Компоненты

- **GraphQL API Gateway** – маршрутизирует запросы на микросервисы (Apollo Server)
- **Микросервис "Пользователи"** – хранение и получение информации о пользователях (PostgreSQL)
- **Микросервис "Заказы"** – управление заказами (MongoDB)
- **Микросервис "Товары"** – список товаров (PostgreSQL)

### Запуск микросервиса 
```bash 
docker compose up -d 
```
### Открытие graphql в браузере 
Users
```bash 
http://localhost:8000/graphql 
```
Orders
```bash 
http://localhost:8001/graphql 
```
Products
```bash 
http://localhost:8002/graphql 
```
# 3. Big Data

## Написана модель линейной регрессии, обучаемая на числовых данных из CSV

# Запуск: 
```bash 
http://localhost:5000
```