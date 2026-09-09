#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
from datetime import datetime
from pathlib import Path
import logging

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import pytz

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

with open('config.json', 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

def load_data(file_path):
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def format_datetime():
    tz = pytz.timezone('Asia/Tehran')
    now = datetime.now(tz)
    return now.strftime('%Y/%m/%d - %H:%M')

def extract_data(text):
    """استخراج داده‌ها با regex بسیار flexible"""
    
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    result = {}
    
    if len(lines) >= 1:
        result['username'] = re.sub(r'[^a-zA-Z0-9آ-یء]', '', lines[0]) or lines[0]
    
    if len(lines) >= 2:
        match = re.search(r'(\d+[.,]?\d*)', lines[1])
        result['amount'] = match.group(1) if match else lines[1]
    
    if len(lines) >= 3:
        match = re.search(r'(\d+)', lines[2])
        result['tokens'] = match.group(1) if match else lines[2]
    
    if len(lines) >= 4:
        result['wallet'] = lines[3]
    
    return result if len(result) >= 3 else None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not update.message or (update.message.text and update.message.text.startswith('/')):
            return
        
        text = update.message.text or update.message.caption
        if not text:
            return
        
        thread_id = update.message.message_thread_id if update.message.is_topic_message else None
        
        logger.info(f"📨 پیام: {text[:50]} (Thread: {thread_id})")
        
        data_extracted = extract_data(text)
        if not data_extracted:
            logger.warning("❌ داده استخراج نشد")
            return
        
        username = data_extracted.get('username', 'نامشخص')
        amount = data_extracted.get('amount', 'نامشخص')
        tokens = data_extracted.get('tokens', 'نامشخص')
        wallet = data_extracted.get('wallet', 'نامشخص')
        
        logger.info(f"✅ استخراج: {username} | {amount} | {tokens} | {wallet}")
        
        # ترون - Thread 3
        if thread_id == 3:
            data = load_data(DATA_DIR / 'tron_data.json')
            data.append({'username': username, 'amount': amount, 'tokens': tokens, 'wallet': wallet, 'timestamp': format_datetime()})
            save_data(DATA_DIR / 'tron_data.json', data)
            response = f"✅ **ترون**\n👤 {username}\n💰 {amount}\n🪙 {tokens}\n🏦 {wallet}"
            await update.message.reply_text(response, parse_mode='Markdown')
            await update.message.delete()
            logger.info(f"✅ ترون ذخیره شد")
        
        # تتر - Thread 4
        elif thread_id == 4:
            data = load_data(DATA_DIR / 'tether_data.json')
            data.append({'username': username, 'amount': amount, 'tokens': tokens, 'wallet': wallet, 'timestamp': format_datetime()})
            save_data(DATA_DIR / 'tether_data.json', data)
            response = f"✅ **تتر**\n👤 {username}\n💰 {amount}\n🪙 {tokens}\n🏦 {wallet}"
            await update.message.reply_text(response, parse_mode='Markdown')
            await update.message.delete()
            logger.info(f"✅ تتر ذخیره شد")
        
        # کش 10+ - Thread 6
        elif thread_id == 6:
            data = load_data(DATA_DIR / 'cashout_10plus.json')
            data.append({'username': username, 'amount': amount, 'card': tokens, 'owner': wallet, 'timestamp': format_datetime()})
            save_data(DATA_DIR / 'cashout_10plus.json', data)
            response = f"✅ **کش 10+**\n👤 {username}\n💰 {amount}\n💳 {tokens}\n📝 {wallet}"
            await update.message.reply_text(response, parse_mode='Markdown')
            await update.message.delete()
            logger.info(f"✅ کش 10+ ذخیره شد")
        
        # کش 10- - Thread 8
        elif thread_id == 8:
            data = load_data(DATA_DIR / 'cashout_10minus.json')
            data.append({'username': username, 'amount': amount, 'card': tokens, 'owner': wallet, 'timestamp': format_datetime()})
            save_data(DATA_DIR / 'cashout_10minus.json', data)
            response = f"✅ **کش 10-**\n👤 {username}\n💰 {amount}\n💳 {tokens}\n📝 {wallet}"
            await update.message.reply_text(response, parse_mode='Markdown')
            await update.message.delete()
            logger.info(f"✅ کش 10- ذخیره شد")
        
        # کش کریپتو - Thread 9
        elif thread_id == 9:
            data = load_data(DATA_DIR / 'cashout_crypto.json')
            data.append({'username': username, 'amount': amount, 'wallet': tokens, 'timestamp': format_datetime()})
            save_data(DATA_DIR / 'cashout_crypto.json', data)
            response = f"✅ **کش کریپتو**\n👤 {username}\n💰 {amount}\n📍 {tokens}"
            await update.message.reply_text(response, parse_mode='Markdown')
            await update.message.delete()
            logger.info(f"✅ کش کریپتو ذخیره شد")
    
    except Exception as e:
        logger.error(f"❌ خطا: {e}")

def main():
    logger.info("🚀 شروع...")
    app = Application.builder().token(CONFIG['bots']['tron']['token']).build()
    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, handle_message))
    logger.info("✅ آماده!")
    app.run_polling(allowed_updates=['message'])

if __name__ == '__main__':
    main()
