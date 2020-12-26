from tgbf.plugin import TGBFPlugin
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler


class About(TGBFPlugin):

    INFO_FILE = "info.md"

    def init(self):
        return CommandHandler(self.get_name(), self.about_callback)

    def about_callback(self, update: Update, context: CallbackContext):
        update.message.reply_text(
            text=self.get_resource(self.INFO_FILE),
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            quote=False)
