<template>
  <ul class="post-list" v-if="posts.length">
    <PostItem
      v-for="post in posts"
      :key="post.id"
      :post="post"
      @edit="$emit('edit', $event)"
      @delete="$emit('delete', $event)"
    />
  </ul>
  <p v-else class="empty">게시글이 없습니다.</p>
</template>

<script setup>
import PostItem from './PostItem.vue'

defineProps({
  posts: { type: Array, required: true },
})
defineEmits(['edit', 'delete'])
</script>

<style scoped>
.post-list {
  padding: 0;
}
.empty {
  color: #999;
  text-align: center;
  padding: 20px 0;
}
</style>