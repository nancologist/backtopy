<template>
    <div class="card">
        <h3>{{ status._source.title }}</h3>
        <span>{{ status._source.text }}</span>
        <button class="card__action-btn delete" @click="onDelete">X</button>
        <button class="card__action-btn update" @click="onDelete">E</button>
    </div>
</template>

<script>
export default {
    props: ['status'],
    
    methods: {
      onDelete() {
        const id = this.status._id;
        this.$emit('ondelete', id);
      },

      onEdit() {
        
      }
    }
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

.card__action-btn {
  border: none;
  border-radius: 50%;
  box-shadow: none;
  color: white;
  cursor: pointer;
  line-height: 1.4;
  position: absolute;
  top: 5%;
}

.delete {
  background-color: red;
  right: 1%;
}

.update {
  background-color: orange;
  right: 5%;
}
</style>