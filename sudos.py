from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis un fichier .env (si utilisé en local)
load_dotenv()

# Remplacer par la variable d'environnement qui contient le token
TOKEN = os.getenv("7569276552:AAHoTt8G8zdY5Amc2WkncVMPmUz-eGmCNmQ")

# Vérifier si le token est bien récupéré
if TOKEN is None:
    raise ValueError("Le token n'a pas été trouvé dans les variables d'environnement.")

# Liste des administrateurs autorisés (remplace avec ton ID Telegram)
ADMIN_IDS = [6616189804]  # Remplace par ton propre ID Telegram ou ceux des autres admins

# Dictionnaires pour stocker les options et messages personnalisés
options_personnalisees = {
    1: "𝐀𝐃𝐌𝐈𝐍 😇💫✌️",
    2: "𝐃𝐀𝐑𝐊 𝐖𝐄𝐁 😳",
    3: "𝐇𝐀𝐂𝐊 𝐖𝐈𝐅𝐈 𝐌𝐄𝐓𝐇𝐎𝐃𝐄 😊",
    4: "𝐇𝐀𝐂𝐊 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐐𝐑 💫",
    5: "𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 🗣️",
    6: "𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍 𝐃𝐄 𝐊𝐀𝐋𝐈 𝐋𝐈𝐍𝐔𝐗 ⚡🔥",
    7: "𝐔𝐍𝐁𝐀𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 🤩😋",
    8: "𝐁𝐀𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐌𝐄𝐓𝐇𝐎𝐃𝐄 ✌️🤫",
    9: "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 😯🔰",
    10: "𝐇𝐓𝐌𝐋/𝐂𝐒𝐒 𝐋𝐈𝐄𝐍 𝐓𝐎𝐔𝐒 𝐄𝐍 𝐏𝐃𝐅 🏃‍♂️",
    11: "𝐀𝐏𝐏𝐄𝐍𝐃𝐑𝐄 𝐋'𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐐𝐔𝐄 𝐒𝐄𝐋𝐎𝐍 𝐒𝐔𝐃𝐎𝐒 🤫",
    12: "𝐂𝐎𝐌𝐌𝐄𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐄𝐑 𝐒𝐐𝐋𝐌𝐀𝐏 🤠",
    13: "𝐀𝐏𝐏𝐑𝐄𝐍𝐃𝐑𝐄 𝐋𝐀 𝐏𝐑𝐎𝐆𝐀𝐌𝐌𝐀𝐓𝐈𝐎𝐍 𝐓𝐎𝐔𝐒 𝐋𝐀𝐍𝐆𝐀𝐆𝐄 😳💫",
    14: "𝐀𝐓𝐓𝐀𝐐𝐔𝐄 𝐖𝐄𝐁 𝐃𝐎𝐒",
    15: "𝐇𝐀𝐂𝐊 𝐏𝐇𝐎𝐍𝐄 𝐀𝐍𝐃 𝐏𝐂 𝐏𝐀𝐈𝐃 🔥🤠",
    16: "𝐇𝐀𝐂𝐊 𝐅𝐑𝐄𝐄 𝐅𝐈𝐑𝐄 𝐏𝐇𝐈𝐒𝐇𝐈𝐍𝐆 🎩",
    17: "𝐇𝐀𝐂𝐊 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐏𝐇𝐈𝐒𝐇𝐈𝐍𝐆 💎",
    18: "𝐇𝐀𝐂𝐊 𝐆𝐀𝐋𝐋𝐄𝐑𝐈𝐄 𝐏𝐇𝐈𝐒𝐇𝐈𝐆 🐱",
    19: "𝐇𝐀𝐂𝐊 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 😀",
    20: "𝐌𝐎𝐃𝐄 𝐏𝐀𝐘𝐄𝐌𝐄𝐍𝐓 𝐀𝐂𝐂𝐄𝐏𝐓𝐄𝐑 😍"
}
messages_personnalises = {
    1: "Voici les informations pour Sudos.",
    2: "Voici la liste des Admins.",
    3: "Voici les informations des Groupes.",
    4: "Besoin d'aide ? Voici les options disponibles.",
    5: "Accédez aux Paramètres ici.",
    6: "message à écrit ici",
    7: "message à écrit ici",
    8: "message à écrit ici",
    9: "message à écrit ici",
    10: "message à écrit ici",
    11: "message à écrit ici",
    12: "message à écrit ici",
    13: "message à écrit ici",
    14: "message à écrit ici",
    15: "message à écrit ici",
    16: "message à écrit ici",
    17: "message à écrit ici",
    18: "message à écrit ici",
    19: "message à écrit ici",
    20: "message à écrit ici"
}

# Étapes de la conversation
CHOISIR_OPTION, SAISIR_MESSAGE = range(2)

# Fonction pour vérifier si l'utilisateur est un administrateur
def est_administrateur(user_id):
    return user_id in ADMIN_IDS

# Commande pour démarrer le bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton(name, callback_data=str(key))] for key, name in options_personnalisees.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choisis une option :", reply_markup=reply_markup)

# Commande pour personnaliser les messages des options existantes
async def personnalise(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    if not est_administrateur(user_id):
        await update.message.reply_text("Désolé, vous n'avez pas l'autorisation d'utiliser cette commande.")
        return ConversationHandler.END

    # Affichage des options existantes
    texte_options = "\n".join([f"{key}: {nom}" for key, nom in options_personnalisees.items()])
    await update.message.reply_text(f"Liste des commandes disponibles :\n{texte_options}\n\nChoisissez une option à personnaliser (ex: 1 pour Sudos):")

    return CHOISIR_OPTION

# Gestion de la sélection de l'option
async def choisir_option(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_selection = update.message.text
    try:
        option_num = int(user_selection)
        if option_num in options_personnalisees:
            context.user_data["option_num"] = option_num
            await update.message.reply_text(f"Vous avez choisi '{options_personnalisees[option_num]}'. Entrez le nouveau message pour cette option :")
            return SAISIR_MESSAGE
        else:
            await update.message.reply_text("Numéro d'option invalide. Veuillez réessayer.")
            return CHOISIR_OPTION
    except ValueError:
        await update.message.reply_text("Veuillez entrer un numéro valide.")
        return CHOISIR_OPTION

# Enregistrement du nouveau message pour l'option sélectionnée
async def saisir_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    new_message = update.message.text
    option_num = context.user_data.get("option_num")
    
    if option_num:
        messages_personnalises[option_num] = new_message
        await update.message.reply_text(f"Le message pour '{options_personnalisees[option_num]}' a été mis à jour avec succès !")
    else:
        await update.message.reply_text("Erreur lors de la mise à jour du message.")

    return ConversationHandler.END

# Commande pour créer une nouvelle option
async def cree(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if not est_administrateur(user_id):
        await update.message.reply_text("Désolé, vous n'avez pas l'autorisation d'utiliser cette commande.")
        return

    # Extraction des arguments pour créer une nouvelle commande
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Utilisation : /cree <nom_option> <message>")
        return

    nom_option = args[0]
    message_option = ' '.join(args[1:])
    option_id = len(options_personnalisees) + 1  # Génération d'un nouvel ID

    # Ajout de l'option
    options_personnalisees[option_id] = nom_option
    messages_personnalises[option_id] = message_option

    await update.message.reply_text(f"Nouvelle option '{nom_option}' ajoutée avec succès.")

# Fonction pour gérer les clics sur les boutons
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    option_number = int(query.data)
    response_message = messages_personnalises.get(option_number, "Message non défini pour cette option.")

    await query.edit_message_text(text=response_message)

# Configuration du bot
def main() -> None:
    application = Application.builder().token(7569276552:AAHoTt8G8zdY5Amc2WkncVMPmUz-eGmCNmQ).build()

    # Commande /start
    application.add_handler(CommandHandler("start", start))

    # Commande /cree pour ajouter une nouvelle option
    application.add_handler(CommandHandler("cree", cree))

    # Gestion des boutons
    application.add_handler(CallbackQueryHandler(button))

    # Conversation handler pour personnaliser les options existantes
    personnalisation_handler = ConversationHandler(
        entry_points=[CommandHandler("personnalise", personnalise)],
        states={
            CHOISIR_OPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, choisir_option)],
            SAISIR_MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, saisir_message)],
        },
        fallbacks=[],
    )

    application.add_handler(personnalisation_handler)

    # Démarrage du bot
    application.run_polling()

if __name__ == "__main__":
    main()
