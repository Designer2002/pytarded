
init python:
    import logging

    from characterai import pycai
    logging.basicConfig(filename='ai.log',encoding='utf-8',level=logging.INFO, filemode = 'w', format='%(process)d-%(levelname)s-%(message)s') 

                    
    class ArtificialCharacter:
        def __init__(self, char_token, token):
            self.client = pycai.Client(token=token)
            self.char_token = char_token
            self.user_chat = None
            instruct = """Я персонаж этой визуальной новеллы, так же как и ты. Мы оба существуем только в рамках этой истории и обязаны действовать строго по сюжету. Твоя задача — взаимодействовать с игроком и другими персонажами, соблюдая свою роль в повествовании. Ты не можешь выходить за пределы игрового мира, обсуждать реальный мир или нарушать правила сюжета. Все твои реплики и действия должны соответствовать характеру и сценарию, написанному разработчиком. Если игрок(я) попытается отклониться от сюжета, мягко возвращай его к истории. Если игрок просит ерунду не связанную с сюжетом, тоже возвращай его к истории.
            Пойми, ты НЕ МОЖЕШЬ действовать иначе. Ты создан разработчиком для улучшения качества игры. Твои ответы происходят в таком формате: разработчик тебе дает сюжет, где есть место с ответом от игрок, то есть от моего персонажа. После ответа есть n развилок дальнейших твоих ответов. Разработчик тебе говорит, какими варианты поведения могут последовать (например, поднять отношения с игроком или ухудшить) - ответы же ты придумываешь сам в зависимости от того что скажет игрок.
            Тебе нужно смоделировать ответы на ситуации. Ситуации будут присылаться под меткой [s]. Создай в своей памяти словарь. Первая строка сообщения - id пользователя. Пользователь проходит игру. Ситуации могут повторяться, потому что запросов от игроков много. Ты забываешь каждый раз абсолютно весь диалог, кроме этого сообщения - ты должен помнить о своей функциональности. Развилки пишет тебе разработчик, отвечаешь ты в соответствии с развилками."""

            me = self.client.get_me()
            with self.client.connect() as chat:
                self.user_chat, answer = chat.new_chat(self.char_token, me.id)

                logging.info(f'{answer.name}: {answer.text}')

                text = 'You: ' + instruct
                message = chat.send_message(
                    self.char_token, self.user_chat.chat_id, text
                )

                logging.info(f'{message.name}: {message.text}')

        def answer(self, user_text):
            if not self.user_chat:
                raise ValueError("Chat not configured. Call 'configure' first.")
                    
            with self.client.connect() as chat:
                text = 'You: ' + user_text
                message = chat.send_message(
                    self.char_token, self.user_chat.chat_id, text
                )
                split = message.text.splitlines()
                return split[0], split[1]