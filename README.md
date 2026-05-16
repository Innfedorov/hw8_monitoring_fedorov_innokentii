# Домашнее задание 8. Мониторинг ML-сервиса

## Цель работы
Настроить мониторинг ML-сервиса с использованием Prometheus и Grafana. Реализовать сбор метрики latency, визуализацию p95 перцентиля, настроить алерт при превышении порога. Обнаружить дрифт данных. Попробовать настроить Data Quality Ops (DQOps).

## Структура проекта
monitoring/
├── docker-compose.yml
├── prometheus/
│   ├── prometheus.yml
│   └── alert.rules.yml
├── ml_service/
│   └── ml_service.py
├── screenshots/
│   ├── grafana_dashboard.png
│   └── prometheus_alert.png
└── README.md

## Метрики
- request_processing_seconds — гистограмма времени обработки запроса.
- p95 latency вычисляется запросом:
  histogram_quantile(0.95, sum(rate(request_processing_seconds_bucket[5m])) by (le))

## Алерт
- HighLatency — срабатывает, если p95 latency > 0.5 секунд в течение 1 минуты.
- Правило описано в prometheus/alert.rules.yml.

## Запуск
1. Запустить Prometheus и Grafana:
   docker-compose up -d
2. Запустить ML-сервис:
   cd ml_service
   python ml_service.py
3. Открыть Grafana: http://localhost:3000 (admin/admin)
4. Импортировать дашборд через API (или создать вручную).

## Результаты
- Дашборд с графиком p95 latency — скриншот screenshots/grafana_dashboard.png
- Алерт в Prometheus — скриншот screenshots/prometheus_alert.png

## Примечания
- Дрифт данных обнаружен с помощью KS-теста (сравнение эталонного и текущего распределения признака sepal length).
- DQOps не удалось запустить без платной лицензии, шаг 4 не выполнен.

## Ссылка на репозиторий
https://github.com/Innfedorov/hw8_monitoring_fedorov_innokentii