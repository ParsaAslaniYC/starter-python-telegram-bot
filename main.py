
TOKEN = "6725461751:AAFwo9Q1Nq4lTyB-Mjy6rQQeXzACcHoQjuw"
import telebot
from telebot import types

class Mia:
    def __init__(self):
        MiaRoms = telebot.TeleBot(TOKEN)
        print("Mia is Borned successfully!")
        self.mr = MiaRoms
        @self.mr.message_handler(commands=['start', 'hello'])
        def send_welcome(message):
            self.mr.reply_to(message, "Howdy, do you need my help to find roms?\ni'm here\nMyCommands:\n/about for about\n/rom for showing roms\n/add_rom for adding rom to database\n/kernel to see kernels\n/add_kernel to add missing kernels to list")
        
        @self.mr.message_handler(commands=['rom', 'find'])
        def send_roms(message):
            with open("Mia_Roms.db", 'r') as db:
                rom_list = db.read()
            self.mr.reply_to(message, rom_list)
        @self.mr.message_handler(commands=['about'])
        def send_about(message):
            self.mr.reply_to(message, "I'm Mia! a bot for helping users to find their rom faster!\nMy father's is @itzParsaYC and @BotFather")
        @self.mr.message_handler(commands=['add_rom'])
        def add_rom(message):        
            self.mr.reply_to(message, "Thanks for adding a new rom to my database!\nPlease send the rom as this format:\n<Rom Name>: <Rom Link>")
            @self.mr.message_handler(func=lambda message: True)
            def add(message):
                with open("Mia_Roms.db", "a") as db:
                    db.write("\n\n" + message.text)
                self.mr.reply_to(message, f"Added!")
        @self.mr.message_handler(commands=['kernel'])
        def show_kernel(message):
            with open("Mia_Kernels.db", "r") as db:
                self.mr.reply_to(message, db.read())
        @self.mr.message_handler(commands=['add_kernel'])
        def add_kernel(message):        
            self.mr.reply_to(message, "Thanks for adding a new kernel to my database!\nPlease send the kernel as this format:\n<Kernel Name>:\n    -KSU: <KSU Kernel Link>\n    -nonKSU: <nonKSU Kernel Link>")
            @self.mr.message_handler(func=lambda message: True)
            def add(message):
                with open("Mia_Kernels.db", "a") as db:
                    db.write("\n\n" + message.text)
                self.mr.reply_to(message, f"Added!")
        self.mr.infinity_polling()
Mia()