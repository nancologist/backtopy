<template>
    <div class="card">
        <h3>{{ status._source.title }}</h3>
        <span>{{ status._source.text }}</span>
        <button class="card__del-btn">X</button>
    </div>
</template>

<script>
export default {
    props: ['status']
}
</script>

<style scoped>
.card {
  border: 1px solid gray;
  border-radius: 5px;
  box-shadow: 1px 1px 1px gray;
  margin: 10px auto;
  padding: 10px;
  position: relative;
  width: 600px;
}

.card__del-btn {
  background-color: red;
  border: none;
  border-radius: 50%;
  box-shadow: none;
  color: white;
  cursor: pointer;
  line-height: 1.4;
  position: absolute;
  right: 1%;
  top: 5%;
}
</style>