<template>
    <form class="form" @submit.prevent="handleSubmit">
      <input class="form__ctrl title" v-model="status.title" type="text" placeholder="Choose a title for your status" />
      <textarea class="form__ctrl text" v-model="status.text" placeholder="Describe your status..."></textarea>
      <button class="form__btn" type="submit">POST</button>
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

    methods: {
        handleSubmit() {
            this.$emit('form-submitted', this.status)
            this.status.title = '';
            this.status.text = '';
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

.form__btn {
    display: inline;
    font-weight: 600;
    margin: auto;
    padding: 10px 20px;
}

.title {
    height: 30px;
    padding: 5px 10px;
}

.text {
    height: 100px;
    padding: 10px;
}
</style>
