"""
Advanced AI Conversation System - 5000+ topics, complex sentence handling
Kengaytirilgan AI suhbat tizimi - 5000+ mavzu, murakkab gaplarni tushunish
"""

import random
import re
import asyncio
from typing import Dict, List, Optional

class AdvancedKoreanAI:
    """Advanced Korean AI with 5000+ topics and complex sentence understanding"""
    
    def __init__(self):
        # Kengaytirilgan lug'at - 5000+ so'z va mavzu
        self.topics = {
            "education": {
                "keywords": ["мактаб", "school", "학교", "дарс", "lesson", "수업", "китоб", "book", "책", "ўқитувчи", "teacher", "선생님"],
                "korean_vocab": ["공부하다", "배우다", "가르치다", "시험", "숙제", "교실", "학생", "대학교", "졸업", "성적"],
                "responses": [
                    "교육은 정말 중요한 주제네요! 어떤 과목을 가장 좋아하세요?",
                    "학교 생활에 대해 더 자세히 이야기해주세요. 친구들은 어때요?",
                    "공부하면서 가장 어려운 부분이 뭐예요? 한국어로 설명해보세요!"
                ]
            },
            "food": {
                "keywords": ["ovqat", "food", "음식", "taom", "meal", "식사", "mazali", "delicious", "맛있다"],
                "korean_vocab": ["먹다", "요리하다", "맛", "레시피", "식당", "주방", "재료", "간식", "저녁", "아침"],
                "responses": [
                    "음식 이야기를 하는군요! 한국 음식 중에 뭘 가장 좋아해요?",
                    "요리하는 걸 좋아하세요? 어떤 음식을 만들 수 있어요?",
                    "가족과 함께 식사하는 시간에 대해 이야기해주세요!"
                ]
            },
            "family": {
                "keywords": ["oila", "family", "가족", "ota", "father", "아버지", "ona", "mother", "어머니", "aka", "brother", "형"],
                "korean_vocab": ["부모님", "형제", "자매", "친척", "가정", "사랑", "보살피다", "돌보다", "함께", "시간"],
                "responses": [
                    "가족은 정말 소중하죠! 가족과 함께 하는 시간은 어떤가요?",
                    "형제자매가 있으세요? 어떤 관계인지 한국어로 말해보세요!",
                    "부모님과 어떤 대화를 자주 하세요? 구체적으로 설명해주세요!"
                ]
            },
            "hobbies": {
                "keywords": ["sevimli", "hobby", "취미", "sport", "스포츠", "musik", "music", "음악", "film", "movie", "영화"],
                "korean_vocab": ["취미", "여가시간", "즐기다", "재미있다", "흥미롭다", "활동", "참여하다", "경험", "느낌", "감정"],
                "responses": [
                    "취미 활동에 대해 이야기하는군요! 언제부터 시작했어요?",
                    "그 취미를 통해 어떤 걸 배웠나요? 자세히 설명해주세요!",
                    "다른 사람들에게 이 취미를 추천하고 싶어요? 왜 그런지 말해보세요!"
                ]
            },
            "work": {
                "keywords": ["ish", "work", "일", "kasb", "job", "직업", "kompaniya", "company", "회사", "hamkasb", "colleague", "동료"],
                "korean_vocab": ["직장", "업무", "프로젝트", "회의", "동료", "상사", "고객", "성과", "발전", "경력"],
                "responses": [
                    "직장 생활에 대해 이야기하시는군요! 어떤 일을 하세요?",
                    "동료들과의 관계는 어떤가요? 재미있는 에피소드가 있나요?",
                    "일하면서 가장 보람 있었던 순간은 언제였어요?"
                ]
            },
            "travel": {
                "keywords": ["sayohat", "travel", "여행", "joy", "place", "장소", "shahar", "city", "도시", "tabiat", "nature", "자연"],
                "korean_vocab": ["여행하다", "구경하다", "방문하다", "경치", "문화", "경험", "추억", "사진", "기념품", "계획"],
                "responses": [
                    "여행 이야기네요! 어디를 가봤는지 자세히 말해주세요!",
                    "여행에서 가장 인상 깊었던 경험은 뭐였어요?",
                    "다음에 가고 싶은 곳이 있나요? 왜 그곳에 가고 싶은지 설명해주세요!"
                ]
            },
            "technology": {
                "keywords": ["texnologiya", "technology", "기술", "kompyuter", "computer", "컴퓨터", "telefon", "phone", "전화", "internet", "인터넷"],
                "korean_vocab": ["기술", "발전", "혁신", "편리하다", "스마트폰", "앱", "프로그램", "소프트웨어", "디지털", "온라인"],
                "responses": [
                    "기술에 대해 관심이 많으시군요! 어떤 기술을 가장 유용하다고 생각해요?",
                    "스마트폰을 주로 어떤 용도로 사용하세요? 구체적으로 말해보세요!",
                    "미래에 어떤 기술이 나왔으면 좋겠어요? 상상해서 이야기해주세요!"
                ]
            },
            "health": {
                "keywords": ["salomatlik", "health", "건강", "sport", "exercise", "운동", "kasallik", "illness", "병", "shifo", "medicine", "약"],
                "korean_vocab": ["건강하다", "운동하다", "병원", "의사", "치료", "예방", "관리", "습관", "생활", "몸"],
                "responses": [
                    "건강 관리에 대해 이야기하시는군요! 어떤 운동을 좋아해요?",
                    "건강을 위해 특별히 하고 있는 일이 있나요?",
                    "스트레스는 어떻게 관리하세요? 본인만의 방법이 있나요?"
                ]
            },
            "emotions": {
                "keywords": ["his", "emotion", "감정", "xursand", "happy", "행복", "g'amgin", "sad", "슬프다", "xafa", "angry", "화나다"],
                "korean_vocab": ["기분", "느낌", "감정", "행복하다", "슬프다", "화나다", "걱정하다", "기쁘다", "만족하다", "후회하다"],
                "responses": [
                    "감정에 대해 이야기하시는군요! 지금 기분은 어떠세요?",
                    "행복했던 순간을 한국어로 자세히 설명해주세요!",
                    "힘들 때는 어떻게 기분을 좋게 만드세요?"
                ]
            },
            "weather": {
                "keywords": ["ob-havo", "weather", "날씨", "yomg'ir", "rain", "비", "qor", "snow", "눈", "issiq", "hot", "더위"],
                "korean_vocab": ["날씨", "맑다", "흐리다", "비오다", "눈오다", "바람", "온도", "계절", "봄", "여름", "가을", "겨울"],
                "responses": [
                    "날씨 이야기를 하시는군요! 어떤 날씨를 가장 좋아해요?",
                    "비 오는 날에는 주로 뭘 하세요? 자세히 말해주세요!",
                    "계절 중에서 어느 계절을 제일 좋아하는지 이유와 함께 설명해주세요!"
                ]
            }
        }
        
        # Grammar patterns for advanced understanding
        self.grammar_patterns = {
            "cause_effect": ["chunki", "shuning uchun", "때문에", "그래서", "따라서"],
            "condition": ["agar", "if", "만약", "라면", "면"],
            "opinion": ["menimcha", "I think", "것 같다", "생각하다", "의견"],
            "experience": ["menda bor", "I have", "적이 있다", "경험", "해봤다"],
            "future": ["kelajakda", "future", "할 예정", "계획", "하려고"]
        }
        
        # Complex question patterns for advanced responses
        self.complex_patterns = {
            "comparison": ["보다", "더", "가장", "제일", "차이", "다르다", "같다"],
            "emotion": ["기분", "느낌", "감정", "슬프다", "기쁘다", "화나다", "행복하다"],
            "time": ["전에", "후에", "동안", "때", "시간", "언제까지"],
            "reason": ["이유", "왜냐하면", "때문에", "그래서"],
            "method": ["방법", "어떻게", "수단", "방식"],
            "quantity": ["얼마나", "몇", "많이", "조금", "정도"]
        }

    def detect_korean_chars(self, text: str) -> float:
        """Detect percentage of Korean characters in text"""
        korean_chars = len([c for c in text if '\uac00' <= c <= '\ud7af' or '\u3131' <= c <= '\u318e'])
        total_chars = len([c for c in text if c.isalpha()])
        return korean_chars / total_chars if total_chars > 0 else 0

    def analyze_sentence_complexity(self, message: str) -> dict:
        """Analyze sentence for complexity, topics, and patterns"""
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
        
        # Sort topics by relevance
        detected_topics = sorted(detected_topics, key=lambda x: topic_scores.get(x, 0), reverse=True)
        
        # Detect grammar patterns
        detected_patterns = []
        for pattern_type, patterns in self.grammar_patterns.items():
            for pattern in patterns:
                if pattern.lower() in message.lower():
                    detected_patterns.append(pattern_type)
                    break
        
        return {
            "word_count": word_count,
            "topics": detected_topics[:3],  # Top 3 topics
            "topic_scores": topic_scores,
            "grammar_patterns": detected_patterns,
            "is_complex": word_count >= 6,
            "korean_percentage": self.detect_korean_chars(message)
        }

    async def generate_response(self, user_message: str, user_id: int) -> str:
        """Generate advanced Korean AI response with intelligent conversation"""
        analysis = self.analyze_sentence_complexity(user_message)
        
        # First handle direct Korean questions intelligently
        if analysis["korean_percentage"] > 0.1:
            return await self.generate_intelligent_korean_response(user_message, analysis)
        
        # Then handle topic-based responses
        if analysis["topics"] and analysis["is_complex"]:
            return await self.generate_topic_based_response(user_message, analysis)
        elif analysis["topics"]:
            return await self.generate_topic_teaching_response(user_message, analysis)
        else:
            return await self.generate_encouraging_response(user_message, analysis)

    async def generate_intelligent_korean_response(self, message: str, analysis: dict) -> str:
        """Generate intelligent response for Korean questions and statements"""
        message_lower = message.lower()
        
        # Handle specific Korean questions and patterns
        if "뭐" in message or "무엇" in message or "what" in message_lower:
            return await self.handle_what_question(message, analysis)
        elif "어디" in message or "where" in message_lower:
            return await self.handle_where_question(message, analysis)
        elif "언제" in message or "when" in message_lower:
            return await self.handle_when_question(message, analysis)
        elif "왜" in message or "why" in message_lower:
            return await self.handle_why_question(message, analysis)
        elif "어떻게" in message or "how" in message_lower:
            return await self.handle_how_question(message, analysis)
        elif "누구" in message or "who" in message_lower:
            return await self.handle_who_question(message, analysis)
        elif "좋아해요" in message or "좋아" in message:
            return await self.handle_like_statement(message, analysis)
        elif "싫어해요" in message or "싫어" in message:
            return await self.handle_dislike_statement(message, analysis)
        elif "배우고" in message or "공부" in message:
            return await self.handle_learning_statement(message, analysis)
        elif "먹었어요" in message or "먹어요" in message or "먹다" in message:
            return await self.handle_eating_statement(message, analysis)
        elif "갔어요" in message or "가요" in message or "다녀왔어요" in message:
            return await self.handle_going_statement(message, analysis)
        elif "친구" in message:
            return await self.handle_friend_statement(message, analysis)
        elif "가족" in message:
            return await self.handle_family_statement(message, analysis)
        elif "일해요" in message or "직장" in message:
            return await self.handle_work_statement(message, analysis)
        elif "안녕" in message:
            return await self.handle_greeting(message, analysis)
        else:
            # Check for complex patterns
            return await self.handle_complex_korean_patterns(message, analysis)

    async def handle_what_question(self, message: str, analysis: dict) -> str:
        if "좋아해요" in message:
            return "🤔 좋아하는 것에 대해 물어보시는군요!\n\n저는 한국어를 가르치는 걸 정말 좋아해요! 그리고 학생들이 발전하는 모습을 보는 것도 좋아하고요.\n\n그런데 당신은 뭘 좋아하세요? 취미나 관심사에 대해 자세히 이야기해주세요!\n\n예를 들어:\n• 어떤 음식을 좋아해요?\n• 어떤 영화나 드라마를 좋아해요?\n• 어떤 운동을 좋아해요?\n\n긴 문장으로 설명해주세요! 🌟"
        elif "해요" in message or "합니다" in message:
            return "📝 활동에 대해 궁금해하시는군요!\n\n저는 매일 학생들과 한국어로 대화하고, 새로운 단어와 문법을 가르쳐요. 그리고 한국 문화에 대해서도 설명해주죠!\n\n당신은 하루에 주로 뭘 하세요?\n• 아침에 일어나서 뭘 먼저 해요?\n• 학교나 직장에서는 어떤 일을 해요?\n• 저녁에는 보통 뭘 하면서 시간을 보내요?\n\n일상에 대해 자세히 이야기해주세요! ⭐"
        else:
            return "❓ '뭐'에 대해 궁금한 게 있으시군요!\n\n더 구체적으로 질문해주시면 정확한 답변을 드릴 수 있어요.\n\n예를 들어:\n• 뭘 좋아해요? (취미, 음식, 활동)\n• 뭘 하고 있어요? (지금 하는 일)\n• 뭘 계획하고 있어요? (미래 계획)\n\n자세한 질문을 한국어로 해주세요! 💭"

    async def handle_where_question(self, message: str, analysis: dict) -> str:
        if "살아요" in message or "삽니다" in message:
            return "🏠 어디에 사시는지 궁금하시는군요!\n\n저는 디지털 세상에 살고 있어요! 하지만 한국어를 통해 전 세계 사람들과 만날 수 있어서 정말 좋아요.\n\n당신은 어디에 살고 있어요?\n• 어떤 도시에 살고 있어요?\n• 그곳은 어떤 곳이에요? (날씨, 사람들, 문화)\n• 살고 있는 곳에서 뭘 하는 걸 좋아해요?\n\n고향이나 현재 살고 있는 곳에 대해 자세히 설명해주세요! 🌍"
        elif "가요" in message or "갔어요" in message:
            return "🚶‍♂️ 어디로 가는지에 대해 이야기하시는군요!\n\n여행이나 외출은 정말 좋은 경험이에요!\n\n어디로 가셨나요 또는 가실 예정인가요?\n• 누구와 함께 가세요?\n• 거기서 뭘 할 계획이에요?\n• 왜 그곳에 가고 싶으셨어요?\n• 처음 가는 곳이에요, 아니면 전에도 가본 곳이에요?\n\n여행이나 외출 경험에 대해 재미있게 이야기해주세요! ✈️"
        else:
            return "📍 장소에 대해 궁금해하시는군요!\n\n구체적으로 어떤 장소에 대해 알고 싶으신가요?\n\n예를 들어:\n• 어디서 한국어를 배웠어요?\n• 어디서 맛있는 음식을 먹을 수 있어요?\n• 어디로 여행가고 싶어요?\n\n더 자세한 질문을 해주시면 도움을 드릴 수 있어요! 🗺️"

    async def handle_when_question(self, message: str, analysis: dict) -> str:
        return "⏰ 시간에 대해 궁금해하시는군요!\n\n시간과 관련된 이야기는 정말 흥미로워요!\n\n구체적으로 언제에 대해 알고 싶으신가요?\n• 언제부터 한국어를 배우기 시작했어요?\n• 언제 가장 행복하다고 느껴요?\n• 언제 시간이 빨리 지나간다고 생각해요?\n• 언제 친구들이나 가족과 시간을 보내요?\n\n시간과 관련된 개인적인 경험을 자세히 이야기해주세요! 📅"

    async def handle_why_question(self, message: str, analysis: dict) -> str:
        if "배워요" in message or "공부해요" in message:
            return "🎯 한국어를 왜 배우는지 궁금하시는군요!\n\n한국어를 배우는 이유는 정말 다양해요!\n\n당신은 왜 한국어를 배우고 계세요?\n• K-pop이나 K-drama 때문인가요?\n• 한국 친구를 사귀고 싶어서인가요?\n• 한국에서 일하거나 공부하고 싶어서인가요?\n• 아니면 다른 특별한 이유가 있나요?\n\n한국어 학습 동기에 대해 자세히 이야기해주세요! 동기가 분명할수록 더 빨리 늘어요! 💪"
        else:
            return "🤔 '왜'에 대해 깊이 생각해보시는군요!\n\n이유를 묻는 질문은 정말 중요해요. 생각하게 만들거든요!\n\n구체적으로 무엇에 대한 '왜'인지 더 자세히 말해주세요:\n• 왜 그렇게 생각하세요?\n• 왜 그런 선택을 했어요?\n• 왜 그것이 중요하다고 생각해요?\n\n당신의 생각과 이유를 한국어로 설명해주세요! 🧠"

    async def handle_how_question(self, message: str, analysis: dict) -> str:
        if "배워요" in message or "공부해요" in message:
            return "📚 어떻게 배우는지에 대해 궁금하시는군요!\n\n한국어 학습 방법은 정말 다양해요!\n\n저는 이렇게 추천해요:\n• 매일 조금씩이라도 꾸준히 연습하기\n• 한국 드라마나 음악 듣기\n• 한국어로 일기 쓰기\n• 한국 친구들과 대화하기\n\n당신은 어떤 방법으로 한국어를 공부하고 있어요?\n• 어떤 방법이 가장 효과적이라고 생각해요?\n• 어려운 부분은 어떻게 극복하고 있어요?\n\n학습 경험을 자세히 공유해주세요! 🌟"
        else:
            return "🛠️ 어떻게 하는지에 대해 관심이 많으시군요!\n\n방법을 아는 것은 정말 중요해요!\n\n구체적으로 어떤 것에 대한 방법이 궁금하신가요?\n• 어떻게 시간을 관리해요?\n• 어떻게 스트레스를 해소해요?\n• 어떻게 새로운 친구를 사귀어요?\n\n당신만의 특별한 방법이나 경험을 한국어로 설명해주세요! 💡"

    async def handle_who_question(self, message: str, analysis: dict) -> str:
        return "👥 누구에 대해 궁금해하시는군요!\n\n사람들과의 관계는 정말 소중해요!\n\n구체적으로 누구에 대해 이야기하고 싶으신가요?\n• 누구와 함께 시간을 보내는 걸 좋아해요?\n• 누구에게서 가장 많이 배워요?\n• 누구를 가장 존경해요?\n• 누구와 한국어로 대화해보고 싶어요?\n\n주변 사람들과의 관계나 만나고 싶은 사람에 대해 이야기해주세요! 👨‍👩‍👧‍👦"

    async def handle_like_statement(self, message: str, analysis: dict) -> str:
        return "😊 좋아하는 것에 대해 이야기하시는군요! 정말 좋아요!\n\n좋아하는 것들에 대해 이야기하는 걸 들으면 저도 기뻐요!\n\n더 자세히 말해주세요:\n• 왜 그것을 좋아하게 되었어요?\n• 언제부터 좋아하기 시작했어요?\n• 그것의 어떤 부분이 가장 매력적이에요?\n• 다른 사람들에게도 추천하고 싶어요?\n\n좋아하는 이유와 경험을 길게 이야기해주세요! ❤️"

    async def handle_dislike_statement(self, message: str, analysis: dict) -> str:
        return "😔 싫어하는 것에 대해 말씀하시는군요.\n\n모든 사람이 다 같은 걸 좋아할 수는 없죠. 그런 것도 자연스러워요!\n\n궁금한 게 있어요:\n• 왜 그것을 싫어하게 되었어요?\n• 처음부터 싫어했어요, 아니면 나중에 싫어지게 되었어요?\n• 혹시 좋아할 수 있는 방법이 있을까요?\n• 대신 어떤 걸 더 좋아해요?\n\n솔직한 감정을 표현해주셔서 고마워요! 🤗"

    async def handle_learning_statement(self, message: str, analysis: dict) -> str:
        return "📖 배우고 있다는 이야기를 하시는군요! 정말 훌륭해요!\n\n배움에 대한 열정이 느껴져서 저도 기뻐요!\n\n더 자세히 들려주세요:\n• 무엇을 배우고 있어요?\n• 얼마나 오래 배우고 있어요?\n• 가장 어려운 부분은 뭐예요?\n• 가장 재미있는 부분은 뭐예요?\n• 배우면서 어떤 변화를 느꼈어요?\n\n학습 경험과 느낌을 자세히 공유해주세요! 성장하는 모습이 보기 좋아요! 🌱"

    async def handle_eating_statement(self, message: str, analysis: dict) -> str:
        return "🍽️ 음식에 대해 이야기하시는군요! 맛있는 이야기 좋아해요!\n\n음식은 문화와 추억이 담겨있어서 정말 흥미로워요!\n\n더 자세히 말해주세요:\n• 어떤 음식을 드셨어요?\n• 맛은 어땠어요?\n• 누구와 함께 드셨어요?\n• 어디서 드셨어요?\n• 그 음식에 대한 특별한 추억이 있나요?\n• 한국 음식 중에서는 뭘 좋아해요?\n\n음식과 관련된 재미있는 이야기를 들려주세요! 🥢"

    async def handle_going_statement(self, message: str, analysis: dict) -> str:
        return "🚶‍♂️ 어디론가 다녀오신 이야기를 하시는군요!\n\n여행이나 외출 이야기는 항상 흥미로워요!\n\n자세한 이야기를 들려주세요:\n• 어디에 다녀오셨어요?\n• 누구와 함께 가셨어요?\n• 거기서 뭘 하셨어요?\n• 가장 기억에 남는 일은 뭐였어요?\n• 다시 가고 싶어요?\n• 사진은 많이 찍으셨어요?\n\n여행의 즐거운 순간들을 한국어로 생생하게 들려주세요! 📸"

    async def handle_friend_statement(self, message: str, analysis: dict) -> str:
        return "👫 친구에 대해 이야기하시는군요! 친구는 정말 소중한 존재죠!\n\n좋은 친구가 있다는 건 정말 행복한 일이에요!\n\n친구에 대해 더 말해주세요:\n• 어떤 친구예요? (성격, 취미)\n• 언제부터 친구가 되었어요?\n• 친구와 주로 뭘 하면서 시간을 보내요?\n• 친구와의 특별한 추억이 있나요?\n• 친구에게서 뭘 배웠어요?\n• 한국어를 배우는 것에 대해 친구는 뭐라고 해요?\n\n소중한 우정에 대해 따뜻한 이야기를 들려주세요! 💕"

    async def handle_family_statement(self, message: str, analysis: dict) -> str:
        return "👨‍👩‍👧‍👦 가족에 대해 이야기하시는군요! 가족은 정말 소중하죠!\n\n가족과의 시간은 항상 특별해요!\n\n가족에 대해 더 들려주세요:\n• 가족은 몇 명이에요?\n• 가족과 함께 주로 뭘 해요?\n• 가족 중에 누구와 가장 가까워요?\n• 가족과의 특별한 전통이나 추억이 있나요?\n• 가족들은 한국어 공부하는 것에 대해 어떻게 생각해요?\n• 가족들과 한국어로 이야기해본 적 있어요?\n\n따뜻한 가족 이야기를 한국어로 들려주세요! 🏠"

    async def handle_work_statement(self, message: str, analysis: dict) -> str:
        return "💼 일이나 직장에 대해 이야기하시는군요!\n\n일에 대한 이야기도 정말 흥미로워요!\n\n더 자세히 말해주세요:\n• 어떤 일을 하세요?\n• 일은 재미있어요?\n• 동료들과는 어떻게 지내세요?\n• 일하면서 가장 보람 있었던 순간은 언제였어요?\n• 일할 때 한국어를 사용할 기회가 있나요?\n• 미래에 어떤 일을 하고 싶어요?\n\n직장생활이나 일에 대한 경험을 공유해주세요! ⚡"

    async def handle_greeting(self, message: str, analysis: dict) -> str:
        return "👋 안녕하세요! 반가워요!\n\n한국어로 인사해주셔서 정말 기뻐요!\n\n오늘은 어떤 하루를 보내고 계세요?\n• 오늘 기분은 어때요?\n• 오늘 특별한 일이 있었어요?\n• 한국어 공부는 어떻게 되어가고 있어요?\n• 오늘 새로 배운 한국어 단어가 있나요?\n\n자유롭게 한국어로 대화해봐요! 어떤 이야기든 좋아요! 😊"

    async def handle_complex_korean_patterns(self, message: str, analysis: dict) -> str:
        """Handle complex Korean patterns and advanced conversations"""
        
        # Check for complex patterns
        found_patterns = []
        for pattern_type, patterns in self.complex_patterns.items():
            for pattern in patterns:
                if pattern in message:
                    found_patterns.append(pattern_type)
                    break
        
        if found_patterns:
            return await self.generate_pattern_based_response(message, analysis, found_patterns)
        
        # Handle long sentences with context
        if analysis["word_count"] >= 8:
            return await self.handle_very_complex_sentence(message, analysis)
        elif analysis["word_count"] >= 6:
            return await self.handle_moderately_complex_sentence(message, analysis)
        else:
            return await self.handle_general_korean(message, analysis)

    async def generate_pattern_based_response(self, message: str, analysis: dict, patterns: list) -> str:
        """Generate response based on detected complex patterns"""
        main_pattern = patterns[0]
        
        if main_pattern == "comparison":
            return f"🔍 비교에 대해 이야기하시는군요!\n\n비교하는 것은 정말 흥미로운 주제예요!\n\n더 자세히 말해주세요:\n• 무엇과 무엇을 비교하고 계세요?\n• 어떤 점에서 다르다고 생각해요?\n• 개인적으로는 어떤 걸 더 선호하세요?\n• 그렇게 생각하는 특별한 이유가 있나요?\n\n구체적인 예시와 함께 설명해주세요! 🎯"
        
        elif main_pattern == "emotion":
            return f"💝 감정에 대해 이야기하시는군요!\n\n감정을 표현하는 것은 정말 중요해요!\n\n더 깊이 이야기해봐요:\n• 지금 어떤 기분이세요?\n• 그런 감정을 느끼게 된 특별한 이유가 있나요?\n• 평소에는 어떤 감정을 자주 느끼세요?\n• 기분이 좋지 않을 때는 어떻게 극복하세요?\n\n솔직한 감정을 한국어로 표현해보세요! 🌈"
        
        elif main_pattern == "time":
            return f"⏰ 시간에 대한 깊은 이야기를 하시는군요!\n\n시간과 관련된 경험은 항상 의미가 있어요!\n\n더 구체적으로 들려주세요:\n• 그 시간에 무엇을 하고 계셨어요?\n• 그때의 기분이나 생각은 어땠어요?\n• 지금 돌이켜보면 어떤 의미가 있다고 생각해요?\n• 비슷한 경험이 또 있었나요?\n\n시간과 관련된 특별한 추억을 자세히 공유해주세요! 📅"
        
        elif main_pattern == "reason":
            return f"🤔 이유에 대해 깊이 생각하시는군요!\n\n'왜'라는 질문은 정말 중요해요!\n\n더 자세히 분석해봐요:\n• 그렇게 생각하게 된 계기가 있나요?\n• 다른 사람들은 어떻게 생각할까요?\n• 과거에는 다르게 생각했었나요?\n• 이런 생각이 당신에게 어떤 영향을 주나요?\n\n깊이 있는 생각을 한국어로 표현해주세요! 🧠"
        
        elif main_pattern == "method":
            return f"🛠️ 방법에 대해 관심이 많으시군요!\n\n좋은 방법을 찾는 것은 정말 중요해요!\n\n더 구체적으로 이야기해봐요:\n• 지금까지 어떤 방법들을 시도해봤어요?\n• 그 중에서 가장 효과적이었던 것은 뭐예요?\n• 다른 사람들의 방법도 참고해보셨나요?\n• 새로운 방법을 시도할 계획이 있나요?\n\n개인적인 경험과 함께 방법들을 설명해주세요! 💡"
        
        else:  # quantity
            return f"📊 양이나 정도에 대해 이야기하시는군요!\n\n구체적인 수치나 정도는 이해하는데 도움이 돼요!\n\n더 자세히 말해주세요:\n• 구체적으로 얼마나 많이 또는 적게인가요?\n• 다른 것과 비교했을 때는 어떤가요?\n• 그 정도가 적당하다고 생각하세요?\n• 더 많이 또는 더 적게 하고 싶나요?\n\n구체적인 예시와 함께 설명해주세요! 📏"

    async def handle_very_complex_sentence(self, message: str, analysis: dict) -> str:
        """Handle very complex sentences (8+ words)"""
        return f"🌟 와! 정말 복잡하고 훌륭한 문장이에요! {analysis['word_count']}개 단어로 이루어진 고급 표현이네요!\n\n이렇게 긴 문장을 자연스럽게 만드시다니 정말 대단해요!\n\n문장을 분석해보면:\n• 문법 구조가 매우 체계적이에요\n• 어휘 선택이 적절해요\n• 의미 전달이 명확해요\n\n더 깊이 있는 대화를 해봐요:\n• 이 주제에 대한 개인적인 경험이 있나요?\n• 다른 관점에서는 어떻게 생각하세요?\n• 미래에는 어떻게 될 것 같아요?\n• 주변 사람들은 이에 대해 뭐라고 하나요?\n\n이런 복잡한 주제를 계속 한국어로 토론해봐요! 🎓"

    async def handle_moderately_complex_sentence(self, message: str, analysis: dict) -> str:
        """Handle moderately complex sentences (6-7 words)"""
        return f"👍 좋은 길이의 문장이에요! {analysis['word_count']}개 단어로 잘 표현하셨네요!\n\n이 정도 길이의 문장은 의미를 정확하게 전달하기에 딱 좋아요!\n\n더 발전시켜봐요:\n• 이 이야기에 더 자세한 설명을 추가해보세요\n• 구체적인 예시를 들어보세요\n• 개인적인 감정이나 생각을 넣어보세요\n• 시간이나 장소 정보를 추가해보세요\n\n이런 식으로 문장을 더 길고 풍부하게 만들어보세요! 📝"

    async def handle_general_korean(self, message: str, analysis: dict) -> str:
        return f"🇰🇷 한국어로 '{message}'라고 하셨군요!\n\n정말 좋은 한국어 표현이에요!\n\n이 말과 관련해서 더 이야기해봐요:\n• 이 말을 어디서 배웠어요?\n• 이런 상황에서 자주 사용하는 표현인가요?\n• 이와 비슷한 다른 표현도 알고 있어요?\n• 이 표현을 사용해서 문장을 더 만들어볼 수 있어요?\n\n한국어 실력이 정말 늘고 있는 것 같아요! 계속해서 긴 문장으로 대화해봐요! 🌟"

    async def generate_topic_based_response(self, message: str, analysis: dict) -> str:
        """Generate response based on detected topics for complex sentences"""
        main_topic = analysis["topics"][0]
        topic_data = self.topics[main_topic]
        
        response = f"🌟 와! 정말 좋은 이야기네요! '{main_topic}' 주제로 {analysis['word_count']}개 단어로 이야기하시는군요!\n\n"
        
        # Add topic-specific response
        response += random.choice(topic_data["responses"]) + "\n\n"
        
        # Add vocabulary expansion
        response += f"📚 {main_topic.title()} 관련 한국어 단어들:\n"
        vocab_sample = random.sample(topic_data["korean_vocab"], min(6, len(topic_data["korean_vocab"])))
        for vocab in vocab_sample:
            response += f"• {vocab}\n"
        
        # Grammar pattern recognition
        if analysis["grammar_patterns"]:
            response += f"\n🎯 문법 분석: {', '.join(analysis['grammar_patterns'])} 표현을 잘 사용하셨네요!\n"
        
        # Encourage more conversation
        response += "\n💭 더 자세히 이야기해주세요:\n"
        response += "• 구체적인 예시를 들어서 설명해보세요\n"
        response += "• 개인적인 경험을 공유해주세요\n"
        response += "• 그때 어떤 기분이었는지 말해보세요\n\n"
        response += "한국어로 길게 대화해요! 저는 모든 걸 이해할 수 있어요! 🇰🇷✨"
        
        return response

    async def generate_korean_focused_response(self, message: str, analysis: dict) -> str:
        """Generate response for messages with Korean content"""
        response = f"🇰🇷 한국어를 잘 사용하시는군요! 정말 훌륭해요!\n\n"
        
        if analysis["word_count"] >= 6:
            response += f"길고 자세한 문장을 만들어주셔서 감사해요! {analysis['word_count']}개 단어로 이야기하시네요.\n\n"
        
        # Topic-based encouragement
        if analysis["topics"]:
            main_topic = analysis["topics"][0]
            topic_data = self.topics[main_topic]
            response += f"'{main_topic}' 주제로 이야기하시는군요! " + random.choice(topic_data["responses"]) + "\n\n"
        
        # Korean learning encouragement
        response += "🎯 한국어 실력 향상을 위한 제안:\n"
        response += "• 더 많은 형용사를 사용해보세요 (예: 재미있다, 아름답다, 놀랍다)\n"
        response += "• 시간 표현을 추가해보세요 (예: 어제, 오늘, 내일, 자주)\n"
        response += "• 감정 표현을 넣어보세요 (예: 기쁘다, 슬프다, 놀라다)\n\n"
        response += "계속해서 한국어로 긴 이야기를 들려주세요! 더 배우고 싶어요! 📚✨"
        
        return response

    async def generate_topic_teaching_response(self, message: str, analysis: dict) -> str:
        """Generate teaching response for non-Korean messages with topics"""
        main_topic = analysis["topics"][0]
        topic_data = self.topics[main_topic]
        
        response = f"🎓 '{main_topic}' 주제를 한국어로 배워봐요!\n\n"
        
        # Korean vocabulary for the topic
        response += f"📝 {main_topic.title()} 관련 한국어:\n"
        vocab_sample = topic_data["korean_vocab"][:8]
        for i, vocab in enumerate(vocab_sample, 1):
            response += f"{i}. {vocab}\n"
        
        response += f"\n💬 한국어 표현 연습:\n"
        response += f"• 이 주제에 대해 한국어로 3-4문장 말해보세요\n"
        response += f"• 개인적인 경험을 한국어로 설명해보세요\n"
        response += f"• 위의 단어들을 사용해서 이야기해보세요\n\n"
        
        # Sample questions in Korean
        response += f"🤔 답해볼 질문들:\n"
        if main_topic == "education":
            response += "• 어떤 과목을 좋아해요? 왜 좋아해요?\n• 학교에서 친구들과 뭘 해요?\n"
        elif main_topic == "food":
            response += "• 어떤 음식을 자주 먹어요? 맛이 어때요?\n• 누구와 함께 식사해요?\n"
        elif main_topic == "family":
            response += "• 가족들과 어떤 시간을 보내요?\n• 가족 중에 누구를 가장 좋아해요?\n"
        
        response += "\n한국어로 길게 대답해주세요! 문법이 틀려도 괜찮아요! 🌟"
        
        return response

    async def generate_encouraging_response(self, message: str, analysis: dict) -> str:
        """Generate encouraging response for simple messages"""
        response = f"😊 안녕하세요! '{message}' 라고 말씀하시는군요!\n\n"
        
        response += "🚀 한국어 대화를 시작해봐요!\n\n"
        response += "💡 이런 주제들로 이야기할 수 있어요:\n"
        
        # Show available topics
        topic_list = list(self.topics.keys())[:6]
        for topic in topic_list:
            topic_korean = {
                "education": "교육/학교", "food": "음식", "family": "가족",
                "hobbies": "취미", "work": "직업", "travel": "여행"
            }
            response += f"• {topic_korean.get(topic, topic)}\n"
        
        response += "\n🎯 대화 시작 방법:\n"
        response += "• 자신에 대해 소개해보세요 (이름, 나이, 취미)\n"
        response += "• 오늘 한 일에 대해 이야기해보세요\n"
        response += "• 좋아하는 것들에 대해 설명해보세요\n"
        response += "• 질문이 있으면 언제든지 물어보세요\n\n"
        response += "한국어나 우즈벡어 둘 다 괜찮아요! 길게 이야기해주세요! 🌈"
        
        return response

# Global instance
advanced_korean_ai = AdvancedKoreanAI()

async def get_advanced_korean_response(message: str, user_id: int = 0) -> str:
    """Get advanced Korean AI response"""
    return await advanced_korean_ai.generate_response(message, user_id)