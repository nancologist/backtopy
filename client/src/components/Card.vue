<template>
    <div class="card" :style="grayedOut">
        <h3>{{ status._source.title }}</h3>
        <span>{{ status._source.text }}</span>
        <button class="card__action-btn delete" @click="onDelete">X</button>
        <button class="card__action-btn update" @click="onEdit">E</button>
    </div>
</template>

<script>
export default {
    props: ['status'],

    computed: {
      grayedOut() {
        const sOnEdit = this.$store.state.statusOnEdit;
        const isEditingCard = !!sOnEdit && 
          this.status._id === sOnEdit._id;
        if (isEditingCard) {
          return { opacity: 0.6 }
        }
        return {};
      }
    },
    
    methods: {
      onDelete() {
        const id = this.status._id;
        this.$emit('ondelete', id);
      },

      onEdit() {
        const id = this.status._id;
        this.$store.commit('setStatusOnEdit', id);
      },
    },
}
</script>

<style scoped>
.card {
  border: 1px solid gray;
  border-radius: 5px;
  box-shadow: 1px 1px 1px gray;
  margin: 10px auto;
  padding: 20px;
  position: relative;
  width: 600px;
}

.card__action-btn {
  border: none;
  border-radius: 50%;
  box-shadow: none;
  color: white;
  cursor: pointer;
  line-height: 0.6;
  position: absolute;
  padding: 5px;
  top: 7%;
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