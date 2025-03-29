# Backend документация

- Здесь можно найти основную информация по установке бекенда мониторинга за аквакультурой и его эндпоинтах.
- Frontend репозиторий мониторинга за аквакультурой https://github.com/noobweer/fishfarm-frontend

### **Устновка на Windowns/Ubuntu**
- Делается🥰

### **API Endpoints**

**POST login/**
- Принимает JSON из username, password, если данные верны, то возвращает JSON из access, refresh токенов.
###### Запрос
```json
{
  "username": "Имя пользователя",
  "password": "Пароль"
}
```
###### Ответ
```json
{
  "refresh": "Значение refresh токена",
  "access": "Значение access токена"
}
```

**POST token/refresh/**
- Принимает JSON с refresh токеном, и возвращает валидный access токен.
###### Запрос
```json
{	
  "refresh":"значение refresh токена"
}
```
###### Ответ
```json
{
  "access": "Значение нового access токена"
}
```

**GET all-pools/**
- Возвращает JSON со списком всех бассейнов состоящий из pool_id, pool_name, pool_desc.
###### Ответ
```json
{
  "data_type": "[{'pool_id': 1, 'pool_name': 'Бассейн №1', 'pool_desc': 'Ряд 1, секция 3'}, {'pool_id': 2, 'pool_name': 'Бассейн №2', 'pool_desc': 'Ряд 2, секция 3'}]"
}
```

**GET status/**
- Обязателен query parametr pool_id.
- Возвращает JSON c pool_id, timestamp, датчиками и их значениями (sensor_id, min_value, max_value, value, zone).
###### Query parametr
```text
pool_id=2
```
###### Ответ
```json
{
  "pool_id": 2,
  "timestamp": "2025-03-01T12:17:53.855673Z",
  "temperature": {
    "sensor_id": null,
    "min_value": 10,
    "max_value": 24,
    "value": 3,
    "zone": "red"
  }
}
```

**POST update/**
- Принимает JSON с pool_id, sensor, minValue, maxValue
- Меняет минимально/макисмально допустимые значения датчика и возвращает JSON с is_updated, который показывает выполнен, что запрос успешно или нет, а также message с комментарием.
###### Запрос
```json
{
  "pool_id": 2,
  "sensor": "temperature",
  "minValue": 15,
  "maxValue": 40
}
```

###### Ответ
```json
{
  "is_updated": true,
  "message": "pool_data 2 changed category:temperature"
}
```
**POST setting/**
- Принимает JSON c pool_id, pool_name, pool_desc, чтобы поменять название или описание бассейна.
- Возвращает JSON с is_updated, который показывает выполнен, что запрос успешно или нет, а также message с комментарием.
###### Запрос
```json
{
  "pool_id": "1",
  "pool_name": "Бассейн №1",
  "pool_desc": "Ряд 1, Секция 3"
}
```
###### Ответ
```json
{
  "is_updated": true,
  "message": "pool 1 changed"
}
```

**POST sensors-data/**
- Принимает JSON с pool_id и датчиками с их значениями.
- Возвращает JSON с is_success, который показывает выполнен, что запрос успешно или нет.
###### Запрос
```json
{
  "pool_id": 1,
  "temperature": 25.3
}
```
###### Ответ
```json
{
  "is_success": true
}
```
**POST thing-state/**
- Принимает JSON с pool_id, thing_name.
- озвращает JSON с is_success, который показывает выполнен, что запрос успешно или нет, а также булевый state, в котором false = Устройство ВЫКЛ, а true = Устройство ВКЛ. 
###### Запрос
```json
{
  "pool_id": 1,
  "thing_name": "freezer"
}
```
###### Ответ
```json
{
  "is_success": true,
  "state": false
}
```