from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from typing import cast
import asyncio
import aiosqlite

from database import get_user, get_user_stats, DATABASE_PATH
from config import PREMIUM_PRICE_UZS
from keyboards import get_main_menu
from messages import PREMIUM_INFO_MESSAGE, REFERRAL_MESSAGE

router = Router()

@router.callback_query(F.data == "premium_purchase")
async def premium_purchase_handler(callback: CallbackQuery):
    """Premium sotib olish"""
    try:
        if not callback.message or not callback.from_user:
            await callback.answer("Xatolik yuz berdi!")
            return
            
        purchase_text = f"""💎 <b>PREMIUM OBUNANI SOTIB OLISH</b>

🎯 <b>Premium narxi:</b> {PREMIUM_PRICE_UZS:,} so'm/oy

💳 <b>To'lov ma'lumotlari:</b>
Karta: 4278 3100 2775 4068
Bank: Kapital Bank (Visa)
Egasi: HOSHIMJON MAMADIYEV

📋 <b>To'lov qilish tartibi:</b>
1️⃣ Yuqoridagi kartaga pul o'tkazing
2️⃣ Screenshot ga oling  
3️⃣ Adminga yuboring: @chang_chi_won
4️⃣ Premium aktivlashtiriladi (24 soat ichida)

⚡ <b>Premium bilan nima olasiz:</b>
• 🤖 AI suhbat (Korean/Japanese)
• 📚 Barcha premium bo'limlar
• 🧠 Maxsus testlar va materiallar
• 📊 Kengaytirilgan statistika
• 🚫 Reklama yo'q

💡 <b>Eslatma:</b> To'lovdan keyin admin bilan bog'laning!"""

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="👤 Admin bilan bog'lanish", url="https://t.me/chang_chi_won")],
            [InlineKeyboardButton(text="👥 Bepul olish (Referral)", callback_data="referral_info")],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="premium")]
        ])
        
        message = cast(Message, callback.message)
        await message.edit_text(
            purchase_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
        await callback.answer()
        
    except Exception as e:
        print(f"Premium purchase error: {e}")
        await callback.answer("❌ Xatolik yuz berdi!", show_alert=True)

@router.callback_query(F.data == "referral_info")
async def referral_info_handler(callback: CallbackQuery):
    """Referral ma'lumotlari"""
    try:
        if not callback.message or not callback.from_user:
            await callback.answer("Xatolik yuz berdi!")
            return
            
        user_id = callback.from_user.id
        user_stats = await get_user_stats(user_id)
        
        if not user_stats:
            await callback.answer("❌ Foydalanuvchi ma'lumotlari topilmadi!")
            return
        
        # Safe tuple unpacking
        try:
            referral_count = user_stats[15] if user_stats and len(user_stats) > 15 else 0
        except (IndexError, KeyError, TypeError):
            referral_count = 0
            
        remaining_referrals = max(0, 10 - referral_count)
        
        # Generate referral code if not exists
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute("SELECT referral_code FROM users WHERE user_id = ?", (user_id,))
            result = await cursor.fetchone()
            
            if result and result[0]:
                referral_code = result[0]
            else:
                import string
                import random
                referral_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                await db.execute("UPDATE users SET referral_code = ? WHERE user_id = ?", (referral_code, user_id))
                await db.commit()
        
        referral_text = f"""👥 <b>REFERRAL DASTURI</b>

🎁 <b>Qanday ishlaydi:</b>
10 ta do'stingizni taklif qiling = 1 oy BEPUL Premium!

📊 <b>Sizning natijangiz:</b>
✅ Tayyor referrallar: {referral_count}/10
⏳ Qolgan: {remaining_referrals} ta

🔗 <b>Sizning linkingiz:</b>
<code>https://t.me/KoreYap_ProGradBot?start={referral_code}</code>

📱 <b>Qanday tarqatish:</b>
1️⃣ WhatsApp, Telegram gruppalarga
2️⃣ Instagram, Facebook story'larga  
3️⃣ Do'stlar, oila a'zolariga
4️⃣ Sinfdoshlar, hamkasblaringizga

💬 <b>Taklif matni:</b>
"Koreys va Yapon tilini bepul o'rganing! 
Bu linkni bosing: https://t.me/KoreYap_ProGradBot?start={referral_code}

Ajoyib bot, men ham foydalanyapman! 🚀"

💰 <b>Hisobi:</b>
1 referral = 5,000 so'm tejash
10 referral = 50,000 so'm tejash = BEPUL oy!"""

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📋 Linkni nusxa olish", callback_data="copy_referral_link")],
            [InlineKeyboardButton(text="📊 Referral statistika", callback_data="referral_stats")],
            [InlineKeyboardButton(text="🎁 Mening mukofotlarim", callback_data="my_rewards")],
            [InlineKeyboardButton(text="🔙 Premium menu", callback_data="premium")]
        ])
        
        message = cast(Message, callback.message)
        await message.edit_text(
            referral_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
        await callback.answer()
        
    except Exception as e:
        print(f"Referral info error: {e}")
        await callback.answer("❌ Xatolik yuz berdi!", show_alert=True)

@router.callback_query(F.data == "copy_referral_link")
async def copy_referral_link_handler(callback: CallbackQuery):
    """Referral linkni nusxa olish"""
    try:
        if not callback.from_user:
            await callback.answer("Xatolik yuz berdi!")
            return
            
        user_id = callback.from_user.id
        
        # Get referral code
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute("SELECT referral_code FROM users WHERE user_id = ?", (user_id,))
            result = await cursor.fetchone()
            referral_code = result[0] if result and result[0] else "UNKNOWN"
        
        link_text = f"""🔗 <b>SIZNING REFERRAL LINKINGIZ:</b>

<code>https://t.me/KoreYap_ProGradBot?start={referral_code}</code>

📱 <b>Tarqatish usullari:</b>

<b>WhatsApp/Telegram uchun:</b>
"Koreys/Yapon tilini o'rganmoqchimisiz? 
Bu ajoyib botni sinab ko'ring: 
https://t.me/KoreYap_ProGradBot?start={referral_code}

Men ham foydalanyapman, juda foydali! 🇰🇷🇯🇵"

<b>Instagram Story uchun:</b>
"Til o'rganish vaqti! 🚀
Link bio'da yoki swipe up ⬆️"

<b>Facebook uchun:</b>
"Do'stlar, koreys/yapon tilini bepul o'rganing!
Menga ham yordam bo'ladi 😊
Link: https://t.me/KoreYap_ProGradBot?start={referral_code}"

💡 <b>Maslahat:</b> Haqiqiy tajribangizni baham ko'ring!"""

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📊 Referral hisobot", callback_data="referral_stats")],
            [InlineKeyboardButton(text="🔙 Referral info", callback_data="referral_info")]
        ])
        
        if callback.message:
            message = cast(Message, callback.message)
            await message.edit_text(
                link_text,
                reply_markup=keyboard,
                parse_mode="HTML"
            )
        
        await callback.answer("✅ Link tayyor! Copy-paste qiling", show_alert=True)
        
    except Exception as e:
        print(f"Copy referral link error: {e}")
        await callback.answer("❌ Xatolik yuz berdi!", show_alert=True)

@router.callback_query(F.data == "referral_stats")
async def referral_stats_handler(callback: CallbackQuery):
    """Referral statistika"""
    try:
        if not callback.from_user or not callback.message:
            await callback.answer("Xatolik yuz berdi!")
            return
            
        user_id = callback.from_user.id
        
        # Get referral statistics
        async with aiosqlite.connect(DATABASE_PATH) as db:
            # Total referrals
            cursor = await db.execute("SELECT COUNT(*) FROM referrals WHERE referrer_id = ?", (user_id,))
            total_referrals = (await cursor.fetchone())[0]
            
            # Recent referrals (last 30 days)
            cursor = await db.execute("""
                SELECT COUNT(*) FROM referrals 
                WHERE referrer_id = ? 
                AND created_at > datetime('now', '-30 days')
            """, (user_id,))
            recent_referrals = (await cursor.fetchone())[0]
            
            # Get last few referrals
            cursor = await db.execute("""
                SELECT u.first_name, r.created_at 
                FROM referrals r
                JOIN users u ON r.referred_id = u.user_id
                WHERE r.referrer_id = ?
                ORDER BY r.created_at DESC
                LIMIT 5
            """, (user_id,))
            last_referrals = await cursor.fetchall()
        
        remaining = max(0, 10 - total_referrals)
        progress_bar = "🟩" * min(total_referrals, 10) + "⬜" * remaining
        
        stats_text = f"""📊 <b>REFERRAL STATISTIKA</b>

🎯 <b>Umumiy natija:</b>
{progress_bar} {total_referrals}/10

📈 <b>Batafsil hisobot:</b>
• Jami referrallar: {total_referrals}
• So'nggi 30 kun: {recent_referrals}
• Qolgan: {remaining} ta
• Tejagan pul: {total_referrals * 5000:,} so'm

💰 <b>Mukofotlar:</b>
• Har referral: 5,000 so'm qiymat
• 10 referral: 50,000 so'm (BEPUL premium oy)

📋 <b>So'nggi referrallar:</b>"""

        if last_referrals:
            for name, date in last_referrals:
                # Format date
                try:
                    from datetime import datetime
                    date_obj = datetime.fromisoformat(date.replace('Z', '+00:00'))
                    formatted_date = date_obj.strftime("%d.%m.%Y")
                except:
                    formatted_date = date[:10] if date else "Noma'lum"
                
                stats_text += f"\n• {name or 'Anonim'} - {formatted_date}"
        else:
            stats_text += "\n• Hozircha referrallar yo'q"
        
        stats_text += f"""

🚀 <b>Keyingi qadam:</b>
{remaining} ta do'st taklif qiling va bepul premium oling!"""

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Linkni olish", callback_data="copy_referral_link")],
            [InlineKeyboardButton(text="🎁 Mukofotlarim", callback_data="my_rewards")],
            [InlineKeyboardButton(text="🔙 Referral info", callback_data="referral_info")]
        ])
        
        message = cast(Message, callback.message)
        await message.edit_text(
            stats_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
        await callback.answer()
        
    except Exception as e:
        print(f"Referral stats error: {e}")
        await callback.answer("❌ Xatolik yuz berdi!", show_alert=True)

@router.callback_query(F.data == "my_rewards")
async def my_rewards_handler(callback: CallbackQuery):
    """Mening mukofotlarim"""
    try:
        if not callback.from_user or not callback.message:
            await callback.answer("Xatolik yuz berdi!")
            return
            
        user_id = callback.from_user.id
        
        # Get user statistics and rewards
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute("""
                SELECT COUNT(*) as referral_count,
                       (SELECT is_premium FROM users WHERE user_id = ?) as is_premium,
                       (SELECT premium_expires_at FROM users WHERE user_id = ?) as premium_expires
                FROM referrals 
                WHERE referrer_id = ?
            """, (user_id, user_id, user_id))
            result = await cursor.fetchone()
            
            referral_count = result[0] if result else 0
            is_premium = result[1] if result and len(result) > 1 else False
            premium_expires = result[2] if result and len(result) > 2 else None
        
        # Calculate rewards
        completed_cycles = referral_count // 10
        current_cycle_referrals = referral_count % 10
        total_money_saved = completed_cycles * 50000
        current_cycle_saved = current_cycle_referrals * 5000
        
        rewards_text = f"""🎁 <b>MENING MUKOFOTLARIM</b>

💎 <b>Premium status:</b> {"✅ Faol" if is_premium else "❌ Faol emas"}

📊 <b>Referral hisobi:</b>
• Jami referrallar: {referral_count}
• Tugallangan sikllar: {completed_cycles}
• Joriy sikl: {current_cycle_referrals}/10

💰 <b>Tejagan pul:</b>
• Tugallangan sikllar: {total_money_saved:,} so'm
• Joriy sikl: {current_cycle_saved:,} so'm
• Jami tejashgan: {(total_money_saved + current_cycle_saved):,} so'm

🏆 <b>Yutuqlar:</b>"""

        if completed_cycles > 0:
            rewards_text += f"\n✅ {completed_cycles} marta bepul premium oldingiz!"
        
        if is_premium:
            rewards_text += f"\n💎 Hozir premium faol"
            if premium_expires:
                try:
                    from datetime import datetime
                    expire_date = datetime.fromisoformat(premium_expires.replace('Z', '+00:00'))
                    formatted_expire = expire_date.strftime("%d.%m.%Y")
                    rewards_text += f" ({formatted_expire} gacha)"
                except:
                    pass
        
        remaining_for_next = 10 - current_cycle_referrals
        if remaining_for_next > 0:
            rewards_text += f"""

🎯 <b>Keyingi mukofot:</b>
{remaining_for_next} ta referral qoldi = bepul premium oy!

Progress: {'🟩' * current_cycle_referrals}{'⬜' * remaining_for_next}"""

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📊 Batafsil statistika", callback_data="referral_stats")],
            [InlineKeyboardButton(text="🔗 Referral link", callback_data="copy_referral_link")],
            [InlineKeyboardButton(text="🔙 Referral info", callback_data="referral_info")]
        ])
        
        message = cast(Message, callback.message)
        await message.edit_text(
            rewards_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
        await callback.answer()
        
    except Exception as e:
        print(f"My rewards error: {e}")
        await callback.answer("❌ Xatolik yuz berdi!", show_alert=True)

@router.callback_query(F.data == "premium_features")
async def premium_features_handler(callback: CallbackQuery):
    """Premium imkoniyatlari"""
    try:
        if not callback.message:
            await callback.answer("Xatolik yuz berdi!")
            return
            
        features_text = """💎 <b>PREMIUM IMKONIYATLARI</b>

🤖 <b>AI Suhbat:</b>
• Korean AI - 12,000+ so'z lug'ati
• Japanese AI - hiragana, katakana, kanji
• Grammar checker va tuzatish
• Cultural context va idiomalar
• Real-time conversation practice

📚 <b>Premium bo'limlar:</b>
• Topik 1 & 2 Premium content
• JLPT N5-N1 maxsus materiallar  
• Audio va video darslar
• PDF ko'llanmalar
• Interactive exercises

🧠 <b>Advanced testlar:</b>
• JLPT simulation tests
• Topik preparation exams
• Grammar va vocabulary quizzes
• Speaking practice tests
• Listening comprehension

📊 <b>Analytics va tracking:</b>
• Batafsil progress hisoboti
• Vocabulary expansion tracking
• Study time analytics
• Performance insights
• Goal setting va achievements

⚡ <b>Premium foydalanuvchi tajribasi:</b>
• Reklama yo'q
• Tezkor javob olish
• Priority customer support
• Early access to new features
• Exclusive content

💰 <b>Narx:</b> Faqat 50,000 so'm/oy
🎁 <b>Yoki 10 ta do'st taklif qiling - bepul!</b>"""

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Hozir sotib olish", callback_data="premium_purchase")],
            [InlineKeyboardButton(text="👥 Bepul olish", callback_data="referral_info")],
            [InlineKeyboardButton(text="🔙 Premium menu", callback_data="premium")]
        ])
        
        message = cast(Message, callback.message)
        await message.edit_text(
            features_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
        await callback.answer()
        
    except Exception as e:
        print(f"Premium features error: {e}")
        await callback.answer("❌ Xatolik yuz berdi!", show_alert=True)
