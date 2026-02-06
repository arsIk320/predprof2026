# Docker

## Требования
- Установлен **Docker Desktop** (macOS).

## Запуск
```bash
cd "predprof2026_canteen"

# 2) папка для данных (SQLite + отчёты)
mkdir -p data

# 3) собрать и запустить
docker-compose up --build
```

Открыть в браузере: http://localhost:8000

## Команды
```bash
# запуск в фоне
docker-compose up -d --build

# логи
docker-compose logs -f

# статус контейнера
docker-compose ps

# остановить (данные останутся в ./data)
docker-compose down

# пересборка без кэша
docker-compose build --no-cache
```

## Где хранятся данные
- `./data/canteen.db` — база SQLite
- `./data/reports/` — отчёты
