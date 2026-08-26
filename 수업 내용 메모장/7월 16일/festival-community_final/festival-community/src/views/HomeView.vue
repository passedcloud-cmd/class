<script setup>
import festivalData from '@/data/서울_축제공연행사.json'
import { ref, computed, onMounted, nextTick } from 'vue'
import FestivalMap from '@/components/FestivalMap.vue'
import ChatbotWidget from '@/components/ChatbotWidget.vue' 

// 게시판 관련
import { usePosts } from '../composables/usePosts'
import PostForm from '../components/community/PostForm.vue'
import PostList from '../components/community/PostList.vue'
import SearchBar from '../components/community/SearchBar.vue'
import TagFilter from '../components/community/TagFilter.vue'

// 축제 목록 관련
const festivals = festivalData.items
const isExpanded = ref(false)
const visibleCount = 8

// 카테고리 매핑표 (lclsSystm3 코드 → 테마 이름)
const categoryMap = {
  'EV010100': '전통/역사',
  'EV010400': '전통/역사',
  'EV020100': '전통/역사',
  'EV010500': '자연/꽃',
  'EV010200': '문화예술',
  'EV020200': '문화예술',
  'EV020500': '문화예술',
  'EV020600': '문화예술',
  'EV020700': '문화예술',
  'EV020800': '문화예술',
  'EV020900': '문화예술',
  'EV030100': '전시/박람회',
  'EV030200': '전시/박람회',
  'EV010600': '생활문화',
  'EV030400': '기타행사',
}

function getCategory(festival) {
  return categoryMap[festival.lclsSystm3] || '기타행사'
}

const categories = ['전체', '전통/역사', '자연/꽃', '문화예술', '전시/박람회', '생활문화', '기타행사']
const selectedCategory = ref('전체')

function selectCategory(cat) {
  selectedCategory.value = cat
  isExpanded.value = false
}

const categoryFilteredFestivals = computed(() => {
  if (selectedCategory.value === '전체') return festivals
  return festivals.filter(f => getCategory(f) === selectedCategory.value)
})

const visibleFestivals = computed(() => {
  return isExpanded.value
    ? categoryFilteredFestivals.value
    : categoryFilteredFestivals.value.slice(0, visibleCount)
})

function toggleExpand() {
  isExpanded.value = !isExpanded.value
}

// 북마크 관련 상태
const BOOKMARK_KEY = 'festivalBookmarks'
const bookmarkedIds = ref([])

onMounted(() => {
  const saved = localStorage.getItem(BOOKMARK_KEY)
  if (saved) {
    bookmarkedIds.value = JSON.parse(saved)
  }
})

function isBookmarked(contentid) {
  return bookmarkedIds.value.includes(contentid)
}

function toggleBookmark(contentid) {
  if (isBookmarked(contentid)) {
    bookmarkedIds.value = bookmarkedIds.value.filter(id => id !== contentid)
  } else {
    bookmarkedIds.value = [...bookmarkedIds.value, contentid]
  }
  localStorage.setItem(BOOKMARK_KEY, JSON.stringify(bookmarkedIds.value))
}

const bookmarkedFestivals = computed(() => {
  return festivals.filter(f => bookmarkedIds.value.includes(f.contentid))
})

// 하이라이트 + 이동 관련
const highlightedId = ref(null)

async function scrollToFestival(contentid) {
  selectedCategory.value = '전체'
  isExpanded.value = true

  await nextTick()

  const el = document.getElementById(`festival-${contentid}`)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'center' })
    highlightedId.value = contentid
    setTimeout(() => {
      highlightedId.value = null
    }, 1500)
  }
}

// 게시판 관련
const {
  filteredPosts,
  keyword,
  selectedTag,
  tagOptions,
  generationOptions,
  addPost,
  updatePost,
  deletePost,
} = usePosts()

const editingPost = ref(null)

function handleSubmit({ title, content, generation, tag, password }) {
  if (editingPost.value) {
    updatePost(editingPost.value.id, { title, content, generation, tag })
    editingPost.value = null
  } else {
    addPost({ title, content, generation, tag, password })
  }
}
</script>

<template>
  <div class="page">
    <!-- 1. 제목 + 안내 문구 -->
    <header class="site-header">
      <h1>서울 축제 실시간 혼잡도 커뮤니티</h1>
      <p>서울의 다양한 축제 정보와 실시간 혼잡도를 확인해보세요</p>
    </header>

    <!-- 2. 지도 -->
    <section class="map-section">
      <FestivalMap />
    </section>

    <!-- 3. 게시판 -->
    <section class="board-section">
      <h2>익명 게시판</h2>

      <PostForm
        :editing-post="editingPost"
        :generation-options="generationOptions"
        :tag-options="tagOptions"
        @submit="handleSubmit"
        @cancel-edit="editingPost = null"
      />

      <SearchBar v-model="keyword" />
      <TagFilter v-model="selectedTag" :tag-options="tagOptions" />

      <p class="count">총 {{ filteredPosts.length }}건</p>

      <PostList
        :posts="filteredPosts"
        @edit="editingPost = $event"
        @delete="deletePost"
      />
    </section>

    <!-- 4. 축제 목록 -->
    <section class="festival-section">
      <h2>축제 목록</h2>

      <div class="category-filter">
        <button
          v-for="cat in categories"
          :key="cat"
          :class="['category-btn', { active: selectedCategory === cat }]"
          @click="selectCategory(cat)"
        >
          {{ cat }}
        </button>
      </div>

      <div class="festival-list">
        <div
          v-for="festival in visibleFestivals"
          :key="festival.contentid"
          :id="`festival-${festival.contentid}`"
          :class="['festival-card', { highlighted: highlightedId === festival.contentid }]"
        >
          <button
            class="bookmark-btn"
            :class="{ active: isBookmarked(festival.contentid) }"
            @click="toggleBookmark(festival.contentid)"
            aria-label="북마크"
          >
            {{ isBookmarked(festival.contentid) ? '★' : '☆' }}
          </button>

          
          <h3>{{ festival.title }}</h3>
          <img :src="festival.firstimage" :alt="festival.title" v-if="festival.firstimage" />
          <div class="no-image-placeholder" v-else></div>
          <p>📍 {{ festival.eventplace }}</p>
          <p>📅 {{ festival.eventstartdate }} ~ {{ festival.eventenddate }}</p>
          <p>💰 {{ festival.usetimefestival }}</p>
        </div>
      </div>
      <div class="more-btn-wrapper">
        <button class="more-btn" @click="toggleExpand">
          {{ isExpanded ? '접기' : '더보기' }}
          <span :class="{ 'arrow-up': isExpanded }">▼</span>
        </button>
      </div>
    </section>

    <!-- 5. AI 챗봇 (화면 오른쪽 아래에 고정으로 뜸) -->
    <ChatbotWidget />

    <!-- 6. 북마크한 축제 목록 (화면 오른쪽에 고정, 스크롤해도 따라다님) -->
    <aside class="bookmark-sidebar" v-if="bookmarkedFestivals.length">
      <h3>⭐ 관심 축제 ({{ bookmarkedFestivals.length }})</h3>
      <ul class="bookmark-list">
        <li v-for="festival in bookmarkedFestivals" :key="festival.contentid" class="bookmark-item">
          <span class="bookmark-item-title" @click="scrollToFestival(festival.contentid)">
            {{ festival.title }}
          </span>
          <button class="bookmark-remove" @click="toggleBookmark(festival.contentid)">✕</button>
        </li>
      </ul>
    </aside>
  </div>
</template>

<style scoped>
.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.site-header {
  text-align: center;
  margin-bottom: 32px;
  background: #B5D4F4;
  border-radius: 12px;
  padding: 32px 24px;
}
.site-header h1 {
  font-size: 26px;
  font-weight: 800;
  font-family: 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
  letter-spacing: -0.5px;
  color: #042C53;
  margin-bottom: 8px;
}
.site-header p {
  font-size: 14px;
  color: #0C447C;
}

.map-section {
  margin-bottom: 40px;
}

/* 💡 게시판, 축제 목록을 둥근 박스로 감싸기 */
.board-section,
.festival-section {
  margin-bottom: 40px;
  background: #B5D4F4;
  border: 0.5px solid #dbe4ec;
  border-radius: 16px;
  padding: 24px;
}
.board-section h2,
.festival-section h2 {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 16px;
}

.festival-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.festival-card {
  position: relative;
  background: white;
  border: 0.5px solid #dbe4ec;
  border-radius: 12px;
  padding: 12px;
  transition: border-color 0.15s ease, transform 0.15s ease;
}
.festival-card:hover {
  border-color: #378ADD;
  transform: translateY(-2px);
}
.festival-card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
  background: #eef4fa;
}
.festival-card .no-image-placeholder {
  width: 100%;
  height: 150px;
  border-radius: 8px;
  background: #FAEEDA;
}
.festival-card h3 {
  font-size: 14px;
  font-weight: 500;
  margin: 10px 0 6px;
}
.festival-card p {
  font-size: 12px;
  color: #666;
  margin: 2px 0;
}

.more-btn-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 24px;
}
.more-btn {
  padding: 8px 20px;
  border: 0.5px solid #FAC775;
  border-radius: 20px;
  background: #FAEEDA;
  color: #633806;
  cursor: pointer;
  font-size: 13px;
}
.more-btn:hover {
  background: #FAC775;
  color: #412402;
}

.category-filter {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
.category-btn {
  padding: 6px 16px;
  border: 0.5px solid #ccc;
  border-radius: 20px;
  background: white;
  color: #666;
  cursor: pointer;
  font-size: 13px;
  transition: all 0.15s ease;
}
.category-btn:hover {
  border-color: #378ADD;
  color: #0C447C;
}
.category-btn.active {
  background: #FAC775;
  color: #412402;
  border-color: #EF9F27;
}

.bookmark-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 30px;
  height: 30px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  font-size: 18px;
  color: #999;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
}
.bookmark-btn.active {
  color: #EF9F27;
}

/* 💡 북마크된 카드는 파란 테두리로 강조 */
.festival-card:has(.bookmark-btn.active) {
  border: 2px solid #378ADD;
}

.bookmark-sidebar {
  position: fixed;
  top: 100px;
  right: 24px;
  width: 220px;
  max-height: 60vh;
  overflow-y: auto;
  background: white;
  border: 0.5px solid #dbe4ec;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  z-index: 9999;
}
.bookmark-sidebar h3 {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 12px 0;
  color: #0C447C;
}
.bookmark-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.bookmark-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  padding: 6px 8px;
  background: #FAEEDA;
  border-radius: 6px;
}
.bookmark-item-title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-right: 8px;
  cursor: pointer;
}
.bookmark-item-title:hover {
  color: #378ADD;
  text-decoration: underline;
}
.bookmark-remove {
  border: none;
  background: none;
  color: #999;
  cursor: pointer;
  font-size: 12px;
  flex-shrink: 0;
}
.bookmark-remove:hover {
  color: #ef4444;
}

.festival-card.highlighted {
  animation: highlight-pulse 1.5s ease;
}
@keyframes highlight-pulse {
  0% {
    box-shadow: 0 0 0 3px #378ADD;
    transform: scale(1.02);
  }
  100% {
    box-shadow: none;
    transform: scale(1);
  }
}

@media (max-width: 1400px) {
  .bookmark-sidebar {
    display: none;
  }
}
</style>