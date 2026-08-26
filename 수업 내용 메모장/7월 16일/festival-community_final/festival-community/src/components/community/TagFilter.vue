<template>
  <div class="tag-filter">
    <button
      :class="{ active: modelValue === '전체' }"
      @click="$emit('update:modelValue', '전체')"
    >
      전체
    </button>
    <button
      v-for="tag in tagOptions"
      :key="tag"
      :class="{ active: modelValue === tag }"
      @click="$emit('update:modelValue', tag)"
    >
      #{{ tag }}
    </button>
  </div>
</template>

<script setup>
defineProps({
  modelValue: { type: String, required: true },
  tagOptions: { type: Array, required: true },
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.tag-filter {
  display: flex;
  gap: 6px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}
.tag-filter button {
  padding: 4px 10px;
  border: 1px solid #ddd;
  border-radius: 14px;
  background: #fff;
  cursor: pointer;
  font-size: 13px;
}
.tag-filter button.active {
  background: #FAC775;
  color: #412402;
  border-color: #EF9F27;
}
</style>