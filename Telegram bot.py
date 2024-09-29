import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from search_and_apply import search_and_apply

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your job application bot. Send /cookies to provide your LinkedIn cookies.')

async def handle_cookies(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    linkedin_cookies = context.args
    if not linkedin_cookies:
        await update.message.reply_text('Please send your LinkedIn cookies.')
        return

    # Parse cookies (assuming they're passed as a JSON string)
    try:
        cookies = json.loads(linkedin_cookies[0])
        search_and_apply(cookies)
        await update.message.reply_text('Applied to jobs using your LinkedIn cookies!')
    except json.JSONDecodeError:
        await update.message.reply_text('Invalid cookie format. Please provide valid cookies.')

async def main() -> None:
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cookies", handle_cookies))

    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
