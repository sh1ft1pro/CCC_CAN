# https://discord.com/oauth2/authorize?clien...

# 1487163490916499556
# https://discord.com/oauth2/authorize?client_id=1487163490916499556&scope=bot&permissions=8
# MTQ4NzE2MzQ5MDkxNjQ5OTU1Ng.GYeaX9.CLEKXxti8gCEWBWS7mxXwap7x3r-8TcQCId6Y8

"""
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
"""
import discord
from discord.ext import commands
import time
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
id | род тикета (в разработке)| discord создателя | статус (0 - не принято, 1 - принято, 2 - закрыт) | discord того, кто принял, если еще не приняли, то пишем 0 | содержание |

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


@bot.command(name='заявкавacademy')
async def zaochnik_academy(ctx):
    # Отправляем в ЛС пользователю
    await ctx.author.send("Пишите вашу заявку тут📝")
        
    # Ждем следующее сообщение от пользователя в ЛС
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    msg = await bot.wait_for('message', check=check)
    await ctx.author.send("Ваща заявка успешно отправлена, ожидайте ответа✅")

    # Выводим заявку в консоль    
    message_from_user = msg.content
    file = open("ticket_base.txt", "r", encoding = "utf-8")
    tickets_mass = file.readlines()
    long_tickets_mass = len(tickets_mass) - 1
    last_ticket = tickets_mass[long_tickets_mass].split("|")
    last_ticket_id = int(last_ticket[0])
    print(f"last ticket id = {last_ticket_id}")
    file.close()

    file = open("ticket_base.txt", "a", encoding = "utf-8")
    file.write(f"{last_ticket_id+1}|{msg.author.mention}|{0}|{0}|{msg.content}\n")

@bot.command(name='доступныетикеты')
async def dostupniye_ticket(ctx):
    print("доступныетикеты")
    admin_channel = bot.get_channel(admin_tickets)
    await admin_channel.send("Все доступные тикеты:🎫")
    file = open("ticket_base.txt", "r", encoding = "utf-8")
    tickets_mass = file.readlines()
    
    #проверка тикетов
    for working_ticket in tickets_mass:
        working_ticket_2 = list(working_ticket.split("|"))
        if working_ticket_2[3] == "0":
            await admin_channel.send(working_ticket)

@bot.command(name='принятьтикет')
async def take_ticket(ctx):
    print("принятьтикет")
    await ctx.author.send("Номер тикета, который хотите принять📝")

    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)    
    msg = await bot.wait_for('message', check=check)
    await ctx.author.send("Вы успешно приняли этот тикет✅")

    ticket_take_number = msg.content

    file = open("ticket_base.txt", "r", encoding = "utf-8")
    tickets = file.readlines()
    finder_result = 0
    for i in tickets:
        listed_i = list(i)
        if listed_i[0] == ticket_take_number:
            listed_i[3] = "1"
            listed_i[4] = ctx.author

            final_i = final_i = "".join(str(item) for item in listed_i)
            tickets[finder_result] = final_i
        finder_result += 1
    file.close()

    file = open("ticket_base.txt", "w", encoding = "utf-8")
    file.writelines(tickets)
    file.close()
    
bot.run("")
