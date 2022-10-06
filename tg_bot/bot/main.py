import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, \
    ConversationHandler, MessageHandler, RegexHandler
from utils import commands_func as comm, inline_buttons_func as in_button
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

GET_YOUR_NAME, SECOND = range(2)


def main():
    updater = Updater(token=os.getenv('ARS_BOT_TOKEN'), request_kwargs={
        'proxy_url': f"socks5://{os.getenv('ARS_BOT_PROXY_IP')}:{os.getenv('ARS_BOT_PROXY_PORT')}",
        'urllib3_proxy_kwargs': {
            'assert_hostname': 'False',
            'cert_reqs': 'CERT_NONE',
            'username': os.getenv('ARS_BOT_PROXY_USER_NAME'),
            'password': os.getenv('ARS_BOT_PROXY_PASSWORD')
        }
    })

    dispatcher = updater.dispatcher

    # get available command buttons
    dispatcher.add_handler(CommandHandler("menu", comm.get_menu))

    # get your session information
    dispatcher.add_handler(CommandHandler("timetable", comm.get_time_table))

    # get available sessions timetable
    dispatcher.add_handler(CommandHandler("session_info", comm.get_session_info))

    # get duckiebot session for user
    dispatcher.add_handler(CommandHandler("get_session", comm.get_session))

    # get info about available bots (dts fleet discover)
    dispatcher.add_handler(
        CommandHandler("check_bots", comm.get_available_duckiebots))

    # ping duckiebot - to make sure it works
    # ask duckiebot name for that
    dispatcher.add_handler(CommandHandler("ping", comm.ping_duckiebot))

    # get link to ARS
    dispatcher.add_handler(CommandHandler("link", comm.get_link_to_site))

    # get info about available commands
    dispatcher.add_handler(CommandHandler("help", comm.get_info))

    # inline menu buttons handlers
    dispatcher.add_handler(
        CallbackQueryHandler(in_button.inline_button_get_session_info,
                             pattern="session_info"))
    dispatcher.add_handler(
        CallbackQueryHandler(in_button.inline_button_get_session,
                             pattern="get_session"))
    dispatcher.add_handler(
        CallbackQueryHandler(in_button.inline_button_get_time_table,
                             pattern="timetable"))
    dispatcher.add_handler(
        CallbackQueryHandler(in_button.inline_button_get_available_duckiebots,
                             pattern="check_bots"))
    dispatcher.add_handler(
        CallbackQueryHandler(in_button.inline_button_ping_duckiebot,
                             pattern="ping"))
    dispatcher.add_handler(
        CallbackQueryHandler(in_button.inline_button_get_link_to_site,
                             pattern="link"))

    dispatcher.add_handler(RegexHandler('^(Menu|Help)$', comm.menu_keyboard))

    # handler for first store GitHub name
    start_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", comm.on_start)],
        states={
            GET_YOUR_NAME: [
                MessageHandler(filters=None, callback=comm.save_github_name)]
        }, fallbacks=[CommandHandler("start", comm.on_start)])
    # handler for change GitHub name
    change_name_handler = ConversationHandler(
        entry_points=[CommandHandler("change_name", comm.change_github_name),
                      CallbackQueryHandler(comm.change_github_name,
                                           pattern="change_name")],
        states={
            GET_YOUR_NAME: [
                MessageHandler(filters=None, callback=comm.save_github_name)]
        }, fallbacks=[CommandHandler("change_name", comm.change_github_name)])
    dispatcher.add_handler(start_conv_handler)
    dispatcher.add_handler(change_name_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()