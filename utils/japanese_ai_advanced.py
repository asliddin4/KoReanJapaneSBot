"""
Advanced Japanese AI Conversation System - Complex sentence handling
Kengaytirilgan Yapon AI suhbat tizimi - Murakkab gaplarni tushunish
"""

import random
import re
import asyncio
from typing import Dict, List, Optional

class AdvancedJapaneseAI:
    """Advanced Japanese AI with complex sentence understanding"""
    
    def __init__(self):
        # Japanese topics with vocabulary
        self.topics = {
            "education": {
                "keywords": ["maktab", "school", "学校", "gakkou", "dars", "lesson", "授業", "jugyou", "kitob", "book", "本", "hon"],
                "japanese_vocab": ["勉強する", "学ぶ", "教える", "試験", "宿題", "教室", "学生", "大学", "卒業", "成績"],
                "responses": [
                    "教育について話していますね！どの科目が一番好きですか？",
                    "学校生活についてもっと詳しく教えてください。友達はどうですか？",
                    "勉強していて一番難しい部分は何ですか？日本語で説明してみてください！"
                ]
            },
            "food": {
                "keywords": ["ovqat", "food", "食べ物", "tabemono", "taom", "meal", "食事", "shokuji", "mazali", "delicious", "美味しい", "oishii"],
                "japanese_vocab": ["食べる", "料理する", "味", "レシピ", "レストラン", "台所", "材料", "おやつ", "夕食", "朝食"],
                "responses": [
                    "食べ物の話をしていますね！日本料理の中で何が一番好きですか？",
                    "料理するのが好きですか？どんな食べ物が作れますか？",
                    "家族と一緒に食事する時間について話してください！"
                ]
            },
            "family": {
                "keywords": ["oila", "family", "家族", "kazoku", "ota", "father", "父", "chichi", "ona", "mother", "母", "haha"],
                "japanese_vocab": ["両親", "兄弟", "姉妹", "親戚", "家庭", "愛", "世話する", "一緒に", "時間"],
                "responses": [
                    "家族は本当に大切ですね！家族と一緒に過ごす時間はどうですか？",
                    "兄弟姉妹はいますか？どんな関係か日本語で話してみてください！",
                    "両親とどんな会話をよくしますか？具体的に説明してください！"
                ]
            },
            "hobbies": {
                "keywords": ["sevimli", "hobby", "趣味", "shumi", "sport", "スポーツ", "musik", "music", "音楽", "ongaku"],
                "japanese_vocab": ["趣味", "自由時間", "楽しむ", "面白い", "興味深い", "活動", "参加する", "経験", "感じ", "感情"],
                "responses": [
                    "趣味活動について話していますね！いつから始めましたか？",
                    "その趣味を通じて何を学びましたか？詳しく説明してください！",
                    "他の人にもその趣味を勧めたいですか？なぜそう思うか話してみてください！"
                ]
            },
            "work": {
                "keywords": ["ish", "work", "仕事", "shigoto", "kasb", "job", "職業", "shokugyou", "kompaniya", "company", "会社", "kaisha"],
                "japanese_vocab": ["職場", "業務", "プロジェクト", "会議", "同僚", "上司", "お客様", "成果", "発展", "経歴"],
                "responses": [
                    "職場生活について話していますね！どんな仕事をしていますか？",
                    "同僚との関係はどうですか？面白いエピソードはありますか？",
                    "仕事をしていて一番やりがいを感じた瞬間はいつでしたか？"
                ]
            }
        }
        
        # Japanese complex patterns
        self.complex_patterns = {
            "comparison": ["より", "もっと", "一番", "違い", "違う", "同じ"],
            "emotion": ["気持ち", "感じ", "感情", "悲しい", "嬉しい", "怒る", "幸せ"],
            "time": ["前に", "後で", "間", "時", "時間", "いつまで"],
            "reason": ["理由", "なぜなら", "ので", "から"],
            "method": ["方法", "どうやって", "手段", "やり方"],
            "quantity": ["どのくらい", "何", "たくさん", "少し", "程度"]
        }

    def detect_japanese_chars(self, text: str) -> float:
        """Detect percentage of Japanese characters in text"""
        hiragana = len([c for c in text if '\u3040' <= c <= '\u309f'])
        katakana = len([c for c in text if '\u30a0' <= c <= '\u30ff'])
        kanji = len([c for c in text if '\u4e00' <= c <= '\u9faf'])
        japanese_chars = hiragana + katakana + kanji
        total_chars = len([c for c in text if c.isalpha()])
        return japanese_chars / total_chars if total_chars > 0 else 0

    def analyze_sentence_complexity(self, message: str) -> dict:
        """Analyze Japanese sentence for complexity, topics, and patterns"""
        words = message.split()
        word_count = len(words)
        
        # Detect topics
        detected_topics = []
        topic_scores = {}
        
        for topic_name, topic_data in self.topics.items():
            score = 0
            for keyword in topic_data["keywords"]:
                if keyword.lower() in message.lower():
                    score += 1
            if score > 0:
                topic_scores[topic_name] = score
                detected_topics.append(topic_name)
        
        detected_topics = sorted(detected_topics, key=lambda x: topic_scores.get(x, 0), reverse=True)
        
        # Detect complex patterns
        found_patterns = []
        for pattern_type, patterns in self.complex_patterns.items():
            for pattern in patterns:
                if pattern in message:
                    found_patterns.append(pattern_type)
                    break
        
        return {
            "word_count": word_count,
            "topics": detected_topics[:3],
            "topic_scores": topic_scores,
            "complex_patterns": found_patterns,
            "is_complex": word_count >= 6,
            "japanese_percentage": self.detect_japanese_chars(message)
        }

    async def generate_response(self, user_message: str, user_id: int) -> str:
        """Generate advanced Japanese AI response"""
        analysis = self.analyze_sentence_complexity(user_message)
        
        # Handle Japanese input intelligently
        if analysis["japanese_percentage"] > 0.1:
            return await self.generate_intelligent_japanese_response(user_message, analysis)
        
        # Handle topic-based responses
        if analysis["topics"] and analysis["is_complex"]:
            return await self.generate_topic_based_response(user_message, analysis)
        elif analysis["topics"]:
            return await self.generate_topic_teaching_response(user_message, analysis)
        else:
            return await self.generate_encouraging_response(user_message, analysis)

    async def generate_intelligent_japanese_response(self, message: str, analysis: dict) -> str:
        """Generate intelligent response for Japanese questions and statements"""
        message_lower = message.lower()
        
        # Handle specific Japanese questions and patterns
        if "何" in message or "なに" in message or "what" in message_lower:
            return await self.handle_what_question_japanese(message, analysis)
        elif "どこ" in message or "where" in message_lower:
            return await self.handle_where_question_japanese(message, analysis)
        elif "いつ" in message or "when" in message_lower:
            return await self.handle_when_question_japanese(message, analysis)
        elif "なぜ" in message or "why" in message_lower or "どうして" in message:
            return await self.handle_why_question_japanese(message, analysis)
        elif "どうやって" in message or "how" in message_lower or "どう" in message:
            return await self.handle_how_question_japanese(message, analysis)
        elif "誰" in message or "だれ" in message or "who" in message_lower:
            return await self.handle_who_question_japanese(message, analysis)
        elif "好き" in message:
            return await self.handle_like_statement_japanese(message, analysis)
        elif "嫌い" in message:
            return await self.handle_dislike_statement_japanese(message, analysis)
        elif "勉強" in message or "学ぶ" in message:
            return await self.handle_learning_statement_japanese(message, analysis)
        elif "食べ" in message:
            return await self.handle_eating_statement_japanese(message, analysis)
        elif "行き" in message or "行っ" in message:
            return await self.handle_going_statement_japanese(message, analysis)
        elif "友達" in message:
            return await self.handle_friend_statement_japanese(message, analysis)
        elif "家族" in message:
            return await self.handle_family_statement_japanese(message, analysis)
        elif "こんにちは" in message or "おはよう" in message:
            return await self.handle_greeting_japanese(message, analysis)
        else:
            # Check for complex patterns
            return await self.handle_complex_japanese_patterns(message, analysis)

    async def handle_what_question_japanese(self, message: str, analysis: dict) -> str:
        if "好き" in message:
            return "🤔 好きなことについて聞いていますね！\n\n私は日本語を教えることが本当に好きです！そして学生が上達する姿を見るのも好きです。\n\nあなたは何が好きですか？趣味や興味について詳しく話してください！\n\n例えば：\n• どんな食べ物が好きですか？\n• どんな映画やドラマが好きですか？\n• どんなスポーツが好きですか？\n\n長い文で説明してください！🌟"
        else:
            return "❓ '何'について知りたがっていますね！\n\nもっと具体的に質問してくれれば、正確な答えができます。\n\n例えば：\n• 何が好きですか？（趣味、食べ物、活動）\n• 何をしていますか？（今していること）\n• 何を計画していますか？（将来の計画）\n\n詳しい質問を日本語でしてください！💭"

    async def handle_complex_japanese_patterns(self, message: str, analysis: dict) -> str:
        """Handle complex Japanese patterns"""
        if analysis["complex_patterns"]:
            pattern = analysis["complex_patterns"][0]
            if pattern == "comparison":
                return f"🔍 比較について話していますね！\n\n比較することは本当に興味深いトピックです！\n\nもっと詳しく話してください：\n• 何と何を比較していますか？\n• どんな点で違うと思いますか？\n• 個人的にはどちらをより好みますか？\n• そう思う特別な理由はありますか？\n\n具体的な例と一緒に説明してください！🎯"
            elif pattern == "emotion":
                return f"💝 感情について話していますね！\n\n感情を表現することは本当に大切です！\n\nもっと深く話してみましょう：\n• 今どんな気持ちですか？\n• そんな感情を感じるようになった特別な理由はありますか？\n• 普段はどんな感情をよく感じますか？\n• 気分が良くない時はどうやって乗り越えますか？\n\n正直な感情を日本語で表現してみてください！🌈"
        
        # Handle long sentences
        if analysis["word_count"] >= 8:
            return f"🌟 わあ！本当に複雑で素晴らしい文ですね！{analysis['word_count']}個の単語でできた高級な表現ですね！\n\nこんなに長い文を自然に作るなんて本当にすごいです！\n\n文を分析してみると：\n• 文法構造がとても体系的です\n• 語彙選択が適切です\n• 意味伝達が明確です\n\nもっと深い会話をしてみましょう：\n• このトピックについて個人的な経験はありますか？\n• 他の観点からはどう思いますか？\n• 将来はどうなると思いますか？\n\nこんな複雑なトピックを日本語で続けて議論しましょう！🎓"
        elif analysis["word_count"] >= 6:
            return f"👍 良い長さの文ですね！{analysis['word_count']}個の単語でよく表現されています！\n\nこの程度の長さの文は意味を正確に伝えるのにちょうど良いです！\n\nもっと発展させてみましょう：\n• この話にもっと詳しい説明を追加してみてください\n• 具体的な例を挙げてみてください\n• 個人的な感情や考えを入れてみてください\n\nこのように文をもっと長く豊かにしてみてください！📝"
        else:
            return f"🇯🇵 日本語で '{message}' と言いましたね！\n\n本当に良い日本語表現です！\n\nこの言葉について関連してもっと話してみましょう：\n• この言葉をどこで学びましたか？\n• こんな状況でよく使う表現ですか？\n• これと似た他の表現も知っていますか？\n\n日本語の実力が本当に伸びているようです！🌟"

    # Additional Japanese-specific handlers would go here...
    async def handle_greeting_japanese(self, message: str, analysis: dict) -> str:
        return "👋 こんにちは！会えて嬉しいです！\n\n日本語で挨拶してくれて本当に嬉しいです！\n\n今日はどんな一日を過ごしてますか？\n• 今日の気分はどうですか？\n• 今日特別なことがありましたか？\n• 日本語の勉強はどうですか？\n• 今日新しく覚えた日本語の単語はありますか？\n\n自由に日本語で会話しましょう！どんな話でも良いです！😊"

    async def generate_topic_based_response(self, message: str, analysis: dict) -> str:
        """Generate response based on detected topics for complex sentences"""
        main_topic = analysis["topics"][0]
        topic_data = self.topics[main_topic]
        
        response = f"🌟 わあ！本当に良い話ですね！'{main_topic}' トピックで{analysis['word_count']}個の単語で話していますね！\n\n"
        response += random.choice(topic_data["responses"]) + "\n\n"
        
        # Add vocabulary expansion
        response += f"📚 {main_topic.title()} 関連の日本語単語：\n"
        vocab_sample = random.sample(topic_data["japanese_vocab"], min(6, len(topic_data["japanese_vocab"])))
        for vocab in vocab_sample:
            response += f"• {vocab}\n"
        
        response += "\n💭 もっと詳しく話してください：\n"
        response += "• 具体的な例を挙げて説明してみてください\n"
        response += "• 個人的な経験を共有してください\n"
        response += "• その時どんな気持ちだったか話してみてください\n\n"
        response += "日本語で長く会話しましょう！私は全部理解できます！🇯🇵✨"
        
        return response

    async def generate_topic_teaching_response(self, message: str, analysis: dict) -> str:
        """Generate teaching response for non-Japanese messages with topics"""
        main_topic = analysis["topics"][0]
        topic_data = self.topics[main_topic]
        
        response = f"🎓 '{main_topic}' トピックを日本語で学びましょう！\n\n"
        
        # Japanese vocabulary for the topic
        response += f"📝 {main_topic.title()} 関連の日本語：\n"
        vocab_sample = topic_data["japanese_vocab"][:8]
        for i, vocab in enumerate(vocab_sample, 1):
            response += f"{i}. {vocab}\n"
        
        response += f"\n💬 日本語表現の練習：\n"
        response += f"• このトピックについて日本語で3-4文話してみてください\n"
        response += f"• 個人的な経験を日本語で説明してみてください\n"
        response += f"• 上の単語を使って話してみてください\n\n"
        response += "\n日本語で長く答えてください！文法が間違っても大丈夫です！🌟"
        
        return response

    async def generate_encouraging_response(self, message: str, analysis: dict) -> str:
        """Generate encouraging response for simple messages"""
        response = f"😊 こんにちは！'{message}' と言いましたね！\n\n"
        
        response += "🚀 日本語の会話を始めましょう！\n\n"
        response += "💡 こんなトピックで話せます：\n"
        
        # Show available topics
        topic_list = list(self.topics.keys())[:5]
        for topic in topic_list:
            topic_japanese = {
                "education": "教育/学校", "food": "食べ物", "family": "家族",
                "hobbies": "趣味", "work": "仕事"
            }
            response += f"• {topic_japanese.get(topic, topic)}\n"
        
        response += "\n🎯 会話の始め方：\n"
        response += "• 自分について紹介してみてください\n"
        response += "• 今日したことについて話してみてください\n"
        response += "• 好きなことについて説明してみてください\n\n"
        response += "日本語でもウズベク語でも大丈夫です！長く話してください！🌈"
        
        return response

# Global instance
advanced_japanese_ai = AdvancedJapaneseAI()

async def get_advanced_japanese_response(message: str, user_id: int = 0) -> str:
    """Get advanced Japanese AI response"""
    return await advanced_japanese_ai.generate_response(message, user_id)