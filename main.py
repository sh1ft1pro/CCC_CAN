# https://discord.com/oauth2/authorize?clien...

# 1487163490916499556
# https://discord.com/oauth2/authorize?client_id=1487163490916499556&scope=bot&permissions=8
# MTQ4NzE2MzQ5MDkxNjQ5OTU1Ng.GYeaX9.CLEKXxti8gCEWBWS7mxXwap7x3r-8TcQCId6Y8

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot("!", intents = intents)

#channel_id

admin_tickets = 1487212548385411204

"""
Создание тикетов

1 - тикет на набор в клан
2 - тикет на набор в администрацию клана
3 - жалоба
4 - другое

Вид тикета:
id | род тикета | discord создателя | статус (0 - не принято, 1 - принято, 2 - закрыт) | discord того, кто принял, если еще не приняли, то пишем 0 | содержание |

Команды тикета

!информация - информация общего рода
!заявкавклан - заявка в клан
!заявканамодератора - заявка на модератора
!взятьтикет - взять тикет (может делать только модератор)
!закрытьтикет - закрыть тикет
!написатьпользователю - написать создателю тикета от бота в лс
!критериакадемка" - информация о критериях подачи заявки в клан
"""

@bot.event
async def on_ready():
	print("Bot started to work!")
@bot.event
async def on_message(message):
    if message.content.lower() in ["!информация"]: # информация общего рода
        await message.channel.send("Привет!😜\nТы попал на наш сервер!💎")

    elif "!заявкавacademy" in message.content.lower(): # заявка в клан		
        channel = bot.get_channel(admin_tickets)        
        if channel:
            file = open("ticket_base.txt", "r", encoding = "utf-8")

            tickets_mass = file.readlines()
            long_tickets_mass = len(tickets_mass) - 1
            last_ticket = tickets_mass[long_tickets_mass].split("|")
            last_ticket_id = int(last_ticket[0])
            print(f"last ticket id = {last_ticket_id}")
            file.close()

            file = open("ticket_base.txt", "a", encoding = "utf-8")
            file.write(f"{last_ticket_id+1}|{message.author.mention}|{0}|{0}|{message.content}\n")
            		
            await message.channel.send("Заявка подана успешно, ожидайте ответа!✔️")
        else:
            print(f"Канал с ID {admin_tickets} не найден!")
            await message.channel.send("❌ Ошибка: канал для уведомлений не найден!")
    elif "!тикеты":
        file = open("ticket_base.txt", "r", encoding = "utf-8")
        tickets_mass = file.readlines()
        await message.channel.send(tickets_mass)

bot.run("MTQ4NzE2MzQ5MDkxNjQ5OTU1Ng.GYeaX9.CLEKXxti8gCEWBWS7mxXwap7x3r-8TcQCId6Y8")