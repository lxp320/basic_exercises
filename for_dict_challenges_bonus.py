"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

# Функция для подсчета сообщений каждым пользователем
def user_message_counter(chat_history: list) -> dict:
    user_messages = {}
    # Для каждого сообщения в истории чата ищем автора
    for message in chat_history:
        user_id = message.get("sent_by")
        # Если автор был, то увеличиваем счетчик сообшений
        if user_messages.get(user_id) != None:
            user_messages[user_id] += 1
        # Если это первое обнаруженное сообщение, то счетчик устанавливается на 1
        else:
            user_messages[user_id] = 1
    return user_messages

# Функция определяет кто больше всех написал сообщений
def user_max_message_written(user_message_data: list) -> int:
    # Используем ранее написанную функцию для получения словаря с подготовленными данными
    user_messages = user_message_counter(user_message_data)
    # Ищем максимальное значение, соответствующее ключу
    user_max_message_id = max(user_messages, key = user_messages.get)
    print(f'Больше всех сообщений ({user_messages.get(user_max_message_id)}) написано пользователем с id: {user_max_message_id}')
    return user_max_message_id

if __name__ == "__main__":
    chat_history = generate_chat_history()
    user_max_message_written(chat_history)


