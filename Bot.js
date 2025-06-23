const { Telegraf } = require('telegraf');
const fetch = require('node-fetch');

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.start(async (ctx) => {
  await ctx.reply(`👋 Welcome! Send any prompt and I'll turn it into an image.`);
});

bot.on('text', async (ctx) => {
  const prompt = ctx.message.text;
  await ctx.reply('🎨 Generating image...');

  const width = 512, height = 512;
  const seed = Math.floor(Math.random() * 100000);
  const model = 'flux';
  const url = `https://pollinations.ai/p/${encodeURIComponent(prompt)}?width=${width}&height=${height}&seed=${seed}&model=${model}`;

  await ctx.replyWithPhoto({ url }, {
    caption: `🖼️ Prompt: "${prompt}"`,
    parse_mode: 'Markdown'
  });
});

bot.launch();
console.log('✅ Bot is running on Railway');
