import telebot, random
import pickle
from telebot import types
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import time
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import defaultdict
from webdriver_manager.chrome import ChromeDriverManager
from random import choice


driver = webdriver.Chrome('chrome.driver')
bot = telebot.TeleBot('5668164328:AAFWOgvEkZa23tHdBK_pbUmcEREs4DAzeQc')


for i in range(1, 2):
    url = f'https://nekdo.ru/{i}/'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    anecdots = soup.find_all('div', class_='text')
for anecdot in anecdots:
    print(anecdot.text)
    time.sleep(10)

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://nekdo.ru/')



with open('anecs.pickle', 'rb') as f:
    anecs = pickle.load(f)

@bot.message_handler(commands=['cat'])
def cat(message):
    async def cat(ctx):
        bot.send_message(message.chat.id, await ctx.send('\n'.join(anecs.keys())))


@bot.message_handler(commands=['rand'])
def rand(message):
    async def rand(ctx):
        bot.send_message(message.chat.id, cat=choice(list(anecs.keys())))


@bot.message_handler(commands=['anek'])
def anek(message):
    async def anek(ctx, cat):
        bot.send_message(message.chat.id, anec=choice(anecs[cat]))


bot.polling(non_stop=True)
