<template>
  <div class="chatbot-root">
    <div class="chatbot-container">
      <!-- 챗봇 열기/닫기 플로팅 버튼 -->
      <button @click="toggleChat" class="chatbot-button" aria-label="Open chat">
        <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
      </button>

      <!-- 챗봇 대화창 UI -->
      <transition name="fade">
        <div v-if="isOpen" class="chat-window" @click.stop>
          <header class="chat-header">
            <div class="chat-title">LocalHub 서울 축제 챗봇</div>
            <button class="chat-close" @click="closeChat" aria-label="Close chat">✕</button>
          </header>

          <!-- 대화 내용창 -->
          <div class="chat-body" ref="bodyRef">
            <div v-for="(m, i) in messages" :key="i" :class="['message', m.from]">
              <div class="message-text">{{ m.text }}</div>
            </div>
            <!-- AI가 답변을 고민할 때 뜨는 로딩 말풍선 -->
            <div v-if="isLoading" class="message bot loading">
              <div class="message-text">답변을 생각 중입니다...</div>
            </div>
          </div>

          <!-- 메시지 입력창 -->
          <form class="chat-input" @submit.prevent="sendMessage">
            <input v-model="newMessage" :disabled="isLoading" placeholder="축제에 대해 물어보세요..." autocomplete="off" />
            <button type="submit" :disabled="isLoading">전송</button>
          </form>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
// 💡 구글의 최신 표준 GenAI 라이브러리를 가져옵니다.
import { GoogleGenAI } from '@google/genai'

// 서울 축제 JSON 데이터 로드
import festivalData from '@/assets/data/서울_축제공연행사.json'

const isOpen = ref(false)
const messages = ref([{ from: 'bot', text: '안녕하세요! 서울 축제 챗봇입니다. 무엇이든 물어보세요!' }])
const newMessage = ref('')
const bodyRef = ref(null)
const isLoading = ref(false)

// 💡 .env 파일에 등록한 Gemini API 키를 연결하여 AI 클라이언트를 생성합니다.
const ai = new GoogleGenAI({ apiKey: import.meta.env.VITE_GEMINI_API_KEY })

const toggleChat = async () => {
  isOpen.value = !isOpen.value
  if (isOpen.value) await nextTick(), scrollToBottom()
}

const closeChat = () => {
  isOpen.value = false
}

// 메시지 전송 및 Gemini 답변 받기
const sendMessage = async () => {
  const txt = newMessage.value.trim()
  if (!txt || isLoading.value) return

  // 1. 내가 쓴 글을 먼저 화면에 표시
  messages.value.push({ from: 'user', text: txt })
  newMessage.value = ''
  isLoading.value = true // 로딩 애니메이션 켜기
  await nextTick()
  scrollToBottom()

  try {
    // AI에게 줄 규칙(지침)과 서울 축제 데이터를 주입합니다.
    const systemInstruction = `당신은 서울 지역의 축제 및 행사를 소개해주는 친절한 'LocalHub' 안내원입니다.
    반드시 아래 제공되는 공식 서울 축제 데이터(JSON)만을 기반으로 사실에 입각하여 답변하세요.
    데이터에 없는 축제나 정보에 대해 질문하면 정중하게 "제공된 데이터 범위 내에서는 확인할 수 없습니다"라고 답하세요.
    답변은 친절하고 가독성이 좋게 정리해서 작성해 주세요.

    [공식 서울 축제 데이터]
    ${JSON.stringify(festivalData.items)}`

    // 대화 내역 누적하기
    const chatHistory = messages.value
      .filter(m => m.text !== '안녕하세요! 완전 무료 구글 AI 기반 서울 축제 챗봇입니다. 무엇이든 물어보세요!')
      .map(m => `${m.from === 'user' ? '사용자' : '안내원'}: ${m.text}`)
      .join('\n')

    const promptText = `[이전 대화 기록]\n${chatHistory}\n\n사용자 질문: ${txt}`

    // 2. 구글 제미나이 API 호출하기 (최신 표준 방식)
    const response = await ai.models.generateContent({
      model: 'gemini-3.5-flash', // 가장 빠르고 효율적인 무료 지원 모델
      contents: promptText,
      config: {
        systemInstruction: systemInstruction // 시스템 가이드라인 주입
      }
    })

    // 3. 답변 화면에 출력하기
    messages.value.push({ from: 'bot', text: response.text })

  } catch (error) {
    console.error('Gemini API 에러:', error)
    messages.value.push({ from: 'bot', text: '죄송합니다. 오류가 발생했습니다. .env 파일의 Gemini API 키가 올바른지 확인해 주세요.' })
  } finally {
    isLoading.value = false // 로딩 끄기
    await nextTick()
    scrollToBottom()
  }
}

function scrollToBottom() {
  if (bodyRef.value) {
    bodyRef.value.scrollTop = bodyRef.value.scrollHeight
  }
}
</script>

<style scoped>
/* 기존의 예쁜 스타일 CSS 그대로 유지 */
.chatbot-root { pointer-events: none; }
.chatbot-container { position: fixed; bottom: 24px; right: 24px; z-index: 9999; pointer-events: auto; }
.chatbot-button { width: 60px; height: 60px; background-color: #3b82f6; color: white; border: none; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 6px 18px rgba(0, 0, 0, 0.16); transition: transform 0.15s ease, background-color 0.15s ease; }
.chatbot-button:hover { transform: scale(1.04); background-color: #2563eb; }
.chat-window { width: 360px; height: 500px; position: absolute; right: 0; bottom: 80px; background: #ffffff; border-radius: 12px; box-shadow: 0 18px 40px rgba(2, 6, 23, 0.18); display: flex; flex-direction: column; overflow: hidden; }
.chat-header { height: 56px; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; border-bottom: 1px solid #eef2f7; background: linear-gradient(180deg, #ffffff, #fafafa); }
.chat-title { font-weight: 600; font-size: 15px; color: #0f172a; }
.chat-close { background: transparent; border: none; font-size: 18px; cursor: pointer; color: #475569; }
.chat-body { flex: 1; padding: 12px; overflow-y: auto; background: #f7fafc; display: flex; flex-direction: column; gap: 8px; }
.message { max-width: 78%; padding: 8px 12px; border-radius: 12px; line-height: 1.3; font-size: 14px; white-space: pre-line; }
.message.user { align-self: flex-end; background: #3b82f6; color: white; border-bottom-right-radius: 6px; }
.message.bot { align-self: flex-start; background: #ffffff; color: #0f172a; border-bottom-left-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
.message.bot.loading { color: #64748b; font-style: italic; background: #f1f5f9; }
.chat-input { display: flex; gap: 8px; padding: 10px; border-top: 1px solid #eef2f7; background: #ffffff; }
.chat-input input { flex: 1; padding: 10px 12px; border-radius: 10px; border: 1px solid #e6edf3; outline: none; font-size: 14px; }
.chat-input button { background: #3b82f6; color: white; border: none; padding: 8px 14px; border-radius: 10px; cursor: pointer; font-weight: 500; }
.chat-input button:hover:not(:disabled) { background: #2563eb; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.18s ease, transform 0.18s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(6px) scale(0.98); }
</style>