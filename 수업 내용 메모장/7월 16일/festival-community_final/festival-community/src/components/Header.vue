<template>
  <header>
    <div class="header-inner">
      <h1>서울 페스티벌 커뮤니티</h1>
      <nav>
        <router-link to="/">홈</router-link>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-inner h1 {
  font-size: 20px;
  margin: 0;
}

nav {
  display: flex;
  gap: 16px;
}

nav a {
  text-decoration: none;
  color: inherit;
}
</style>