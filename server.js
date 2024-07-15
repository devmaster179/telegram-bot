const { Telegraf } = require('telegraf');

// Remplacez 'YOUR_BOT_TOKEN' par votre véritable jeton de bot
const BOT_TOKEN = 'Your bot token';

const bot = new Telegraf(BOT_TOKEN);

bot.start((ctx) => {
  const chatId = ctx.message.chat.id;
  const link = 'http://t.me/loot_box_box_bot/LOOTBOX';
  const message = `Hello! Tap here to visit the miniAPP: ${link}`;
  return ctx.reply(message);
});

bot.launch();

console.log('Bot is running...');
