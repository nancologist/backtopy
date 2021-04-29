<template>
<header class="header">
  <h1 class="header__title">Status App</h1>
  <nav class="nav">
    <ul class="nav__list">
      <li class="nav__list__item">
        <router-link exact to="/">Home</router-link>
      </li>
      <li class="nav__list__item">
        <router-link to="/about">About</router-link>
      </li>
      <li class="nav__list__item">
        <router-link to="/user">User</router-link>
      </li>
    </ul>
  </nav>
</header>
</template>

<style scoped>
.header {
  background-color: #333;
  box-shadow: 1px 2px #ccc;
  color: #fff;
  padding: 10px;
}

.nav__list {
  color: #ccc;
  display: flex;
  justify-content: space-evenly;
  margin: 20px auto;
  width: 60%;
}

.nav__list__item {
  border-bottom: 2px solid transparent;
  padding: 2px;
}

.nav__list__item:hover {
  border-bottom: 2px solid white;
}

.router-link-active {
  color: white;
  font-weight: 600;
}
</style>