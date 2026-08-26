<template>
  <li class="post-item">
    <div class="head">
      <span class="tag">#{{ post.tag }}</span>
      <span class="generation">{{ post.generation }}</span>
      <span class="date">{{ formatDate(post.createdAt) }}</span>
    </div>
    <h3>{{ post.title }}</h3>
    <!-- 💡 v-html로 변경, 링크가 있으면 클릭 가능하게 -->
    <p v-html="linkify(post.content)"></p>
    <div class="actions">
      <button @click="handleEdit">수정</button>
      <button @click="handleDelete">삭제</button>
    </div>

    <!-- 댓글 영역 -->
    <div class="comment-section">
      <button class="comment-toggle" @click="showComments = !showComments">
        💬 댓글 {{ post.comments ? post.comments.length : 0 }}개
        {{ showComments ? '숨기기' : '보기' }}
      </button>

      <div v-if="showComments" class="comment-body">
        <ul class="comment-list" v-if="post.comments && post.comments.length">
          <li v-for="comment in post.comments" :key="comment.id" class="comment-item">
            <span class="comment-author">익명</span>
            <!-- 💡 댓글도 링크 변환 적용 -->
            <span class="comment-content" v-html="linkify(comment.content)"></span>
            <span class="comment-date">{{ formatDate(comment.createdAt) }}</span>
            <button
              class="comment-delete"
              @click="handleCommentDelete(comment.id)"
              aria-label="댓글 삭제"
            >
              ✕
            </button>
          </li>
        </ul>
        <p v-else class="no-comment">아직 댓글이 없습니다.</p>

        <form class="comment-form" @submit.prevent="handleCommentSubmit">
          <input
            v-model="newComment"
            type="text"
            placeholder="익명으로 댓글 남기기"
            required
          />
          <input
            v-model="newCommentPassword"
            type="password"
            placeholder="비밀번호"
            class="comment-password-input"
            required
          />
          <button type="submit">등록</button>
        </form>
      </div>
    </div>
  </li>
</template>

<script setup>
import { ref } from 'vue'
import { usePosts } from '../../composables/usePosts'

const props = defineProps({
  post: { type: Object, required: true },
})
const emit = defineEmits(['edit', 'delete'])

const { verifyPassword, addComment, verifyCommentPassword, deleteComment } = usePosts()

const showComments = ref(false)
const newComment = ref('')
const newCommentPassword = ref('')

function formatDate(timestamp) {
  return new Date(timestamp).toLocaleString('ko-KR')
}

// 💡 HTML 특수문자 이스케이프 (보안을 위해 먼저 처리)
function escapeHtml(text) {
  const div = document.createElement('div')
  div.textContent = text
  return div.innerHTML
}

// 💡 텍스트 안의 URL을 찾아 클릭 가능한 링크로 변환
function linkify(text) {
  if (!text) return ''
  const escaped = escapeHtml(text)
  const urlPattern = /(https?:\/\/[^\s<]+)/g
  return escaped.replace(
    urlPattern,
    (url) => `<a href="${url}" target="_blank" rel="noopener noreferrer" class="post-link">${url}</a>`
  )
}

function handleEdit() {
  const input = prompt('비밀번호를 입력하세요')
  if (input === null) return
  if (verifyPassword(props.post.id, input)) {
    emit('edit', props.post)
  } else {
    alert('비밀번호가 일치하지 않습니다.')
  }
}

function handleDelete() {
  const input = prompt('비밀번호를 입력하세요')
  if (input === null) return
  if (verifyPassword(props.post.id, input)) {
    if (confirm('정말 삭제하시겠습니까?')) {
      emit('delete', props.post.id)
    }
  } else {
    alert('비밀번호가 일치하지 않습니다.')
  }
}

function handleCommentSubmit() {
  const text = newComment.value.trim()
  const pw = newCommentPassword.value.trim()
  if (!text || !pw) return
  addComment(props.post.id, text, pw)
  newComment.value = ''
  newCommentPassword.value = ''
  showComments.value = true
}

function handleCommentDelete(commentId) {
  const input = prompt('댓글 비밀번호를 입력하세요')
  if (input === null) return
  if (verifyCommentPassword(props.post.id, commentId, input)) {
    if (confirm('이 댓글을 삭제하시겠습니까?')) {
      deleteComment(props.post.id, commentId)
    }
  } else {
    alert('비밀번호가 일치하지 않습니다.')
  }
}
</script>

<style scoped>
.post-item {
  background: white;
  border: 0.5px solid #dbe4ec;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 10px;
  list-style: none;
}
.head {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #888;
}
.actions {
  margin-top: 8px;
  display: flex;
  gap: 6px;
}
.actions button {
  font-size: 12px;
  cursor: pointer;
}

/* 💡 링크 스타일 */
:deep(.post-link) {
  color: #3b82f6;
  text-decoration: underline;
  word-break: break-all;
}
:deep(.post-link:hover) {
  color: #2563eb;
}

.comment-section {
  margin-top: 10px;
  border-top: 1px dashed #eee;
  padding-top: 8px;
}
.comment-toggle {
  background: none;
  border: none;
  color: #3b82f6;
  font-size: 12px;
  cursor: pointer;
  padding: 0;
}
.comment-body {
  margin-top: 8px;
}
.comment-list {
  list-style: none;
  padding: 0;
  margin: 0 0 8px 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.comment-item {
  background: #f8f9fa;
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 12px;
  display: flex;
  gap: 6px;
  align-items: center;
  flex-wrap: wrap;
}
.comment-author {
  font-weight: bold;
  color: #555;
}
.comment-content {
  flex: 1;
  color: #333;
}
.comment-date {
  font-size: 10px;
  color: #aaa;
}
.comment-delete {
  border: none;
  background: none;
  color: #bbb;
  cursor: pointer;
  font-size: 11px;
  padding: 2px 4px;
  flex-shrink: 0;
}
.comment-delete:hover {
  color: #ef4444;
}
.no-comment {
  font-size: 12px;
  color: #999;
  padding: 8px 0;
}
.comment-form {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.comment-form input {
  padding: 6px 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 12px;
}
.comment-form input[type="text"] {
  flex: 1;
  min-width: 120px;
}
.comment-password-input {
  width: 100px;
}
.comment-form button {
  padding: 6px 12px;
  border: none;
  background: #3b82f6;
  color: white;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
}
</style>