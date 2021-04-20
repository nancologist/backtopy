<template>
    <form class="form" @submit.prevent="handleSubmit">
      <input
        class="form__ctrl title"
        v-model="status.title"
        type="text"
        placeholder="Choose a title for your status"
      />
      <textarea
        class="form__ctrl text"
        v-model="status.text"
        placeholder="Describe your status..."
      ></textarea>
      <button
        class="form__btn"
        :class="submitClass"
        type="submit"
      >
          {{!!editingStatus ? 'EDIT' : 'POST' }}
      </button>
    </form>
</template>

<script>
export default {
    data: () => ({
        status: {
            title: '',
            text: ''
        }
    }),

    props: ['editingStatus'],

    methods: {
        handleSubmit() {
            this.$emit('form-submitted', this.status)
            this.status.title = '';
            this.status.text = '';
        }
    },

    computed: {
        submitClass() {
            return {
                'on-post': !this.editingStatus,
                'on-edit': !!this.editingStatus
            }
        }
    },

    watch: {
        editingStatus(val) {
            const { _source: { text, title } } = val;
            this.status.title = title;
            this.status.text = text;
        }
    }
}
</script>

<style scoped>
.form {
    display: flex;
    flex-direction: column;
    margin: auto;
    width: 500px;
}

.form__ctrl {
    margin: 10px 0;
}

.title {
    height: 30px;
    padding: 5px 10px;
}

.text {
    height: 100px;
    padding: 10px;
}

.form__btn {
    background-color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    display: inline;
    font-weight: 600;
    margin: auto;
    padding: 10px 20px;
}

.form__btn:hover {
    background-color: #f4f4f4;
}

.on-post {
    color: darkgreen;
    border: 2px solid darkgreen;
}

.on-edit {
    color: orangered;
    border: 2px solid orangered;
}
</style>
