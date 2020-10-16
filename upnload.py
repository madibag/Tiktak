import os

def nload(u,c,name,capt):
    chat_id = u.message.chat.id
    context.bot.send_video(chat_id = chat_id,
                                video= open(name, 'rb'),
                                caption = capt
                                )
    os.remove(name)
