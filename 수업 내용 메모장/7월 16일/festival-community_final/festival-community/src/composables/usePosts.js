import { getEffectiveTodayEndTimestamp } from '@/config/demoDate'
import { ref, computed, watch } from 'vue'

const STORAGE_KEY = 'anonymous-board-posts'
const TAG_OPTIONS = ['축제', '음식', '공연', '동행', '기타']
const GENERATION_OPTIONS = [
  ...Array.from({ length: 16 }, (_, i) => `${i + 1}기`),
  'SSAFY무관',
]
function loadPosts() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : []
  } catch (e) {
    console.error('localStorage 파싱 실패:', e)
    return []
  }
}

const posts = ref(loadPosts())

watch(
  posts,
  (newPosts) => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(newPosts))
  },
  { deep: true }
)

export function usePosts() {
  const keyword = ref('')
  const selectedTag = ref('전체')

const filteredPosts = computed(() => {
  const cutoff = getEffectiveTodayEndTimestamp()
  return posts.value
    .filter((p) => p.createdAt <= cutoff) // 💡 설정된 날짜 이후 작성글 숨김
    .filter((p) => {
      if (!keyword.value) return true
      return (
        p.title.includes(keyword.value) || p.content.includes(keyword.value)
      )
    })
    .filter((p) => {
      if (selectedTag.value === '전체') return true
      return p.tag === selectedTag.value
    })
    .sort((a, b) => b.createdAt - a.createdAt)
})

  function addPost({ title, content, tag, password, generation }) {
    posts.value.push({
      id: Date.now(),
      title,
      content,
      tag: tag || '기타',
      generation: generation || 'SSAFY무관',
      createdAt: Date.now(),
      password,
      comments: [],
    })
  }

  function verifyPassword(id, password) {
    const target = posts.value.find((p) => p.id === id)
    if (!target) return false
    return target.password === password
  }

  function updatePost(id, { title, content, tag, generation }) {
    const target = posts.value.find((p) => p.id === id)
    if (!target) return
    target.title = title
    target.content = content
    target.tag = tag
    target.generation = generation
  }

  function deletePost(id) {
    posts.value = posts.value.filter((p) => p.id !== id)
  }

  // 💡 댓글 추가 시 비밀번호도 같이 저장
  function addComment(postId, content, password) {
    const target = posts.value.find((p) => p.id === postId)
    if (!target) return
    if (!target.comments) target.comments = []
    target.comments.push({
      id: Date.now(),
      content,
      password,
      createdAt: Date.now(),
    })
  }

  // 💡 댓글 비밀번호 확인
  function verifyCommentPassword(postId, commentId, password) {
    const post = posts.value.find((p) => p.id === postId)
    if (!post || !post.comments) return false
    const comment = post.comments.find((c) => c.id === commentId)
    if (!comment) return false
    return comment.password === password
  }

  function deleteComment(postId, commentId) {
    const target = posts.value.find((p) => p.id === postId)
    if (!target || !target.comments) return
    target.comments = target.comments.filter((c) => c.id !== commentId)
  }

  return {
    posts,
    filteredPosts,
    keyword,
    selectedTag,
    tagOptions: TAG_OPTIONS,
    generationOptions: GENERATION_OPTIONS,
    addPost,
    updatePost,
    deletePost,
    verifyPassword,
    addComment,
    verifyCommentPassword,
    deleteComment,
  }
}