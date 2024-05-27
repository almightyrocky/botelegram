from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    participants = ['Rocco', 'Marco', 'Ivo']
    zones = ['Ingresso', 'Cucina', 'Bagno']
    
    random.shuffle(zones)
    
    assignment = {participants[i]: zones[i] for i in range(len(participants))}
    
    message = "Che cazzo pulite oggi?\n"
    for participant, zone in assignment.items():
        message += f"{participant}: {zone}\n"
    
    await context.bot.send_message(chat_id=chat_id, text=message)


def main():
    # Inserisci il token del tuo bot
    application = Application.builder().token("6921163208:AAHAjsLHSMuIGQVFST91YX0UtbsVBJhG3YI").build()
    
    # Aggiungi il comando /start al dispatcher
    application.add_handler(CommandHandler("start", start))
    
    # Avvia il bot
    application.run_polling()

if __name__ == '__main__':
    main()
