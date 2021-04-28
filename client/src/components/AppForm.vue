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
      <div class="form__actions">
            <button
                class="form__btn cancel" 
                v-if="!!statusOnEdit"
                @click="cancelEdit"
            >Cancel</button>
            <button
                class="form__btn"
                :class="submitClass"
                type="submit"
            >{{!!statusOnEdit ? 'EDIT' : 'POST' }}</button>
      </div>
    </form>
</template>

<script>
import { mapState } from 'vuex';

export default {
    data: () => ({
        status: {
            title: '',
            text: ''
        }
    }),

    methods: {
        handleSubmit() {
            if (this.statusOnEdit) {
                this.status.id = this.statusOnEdit._id;
            }

            this.$emit('form-submitted', this.status)
            this.status.title = '';
            this.status.text = '';
        },

        cancelEdit() {
            this.status.title = '';
            this.status.text = '';
            this.$emit('cancel-edit');
        }
    },

    computed: {
        submitClass() {
            return {
                'on-post': !this.statusOnEdit,
                'on-edit': !!this.statusOnEdit
            }
        },

        ...mapState([
            'statusOnEdit'
        ])
    },

    watch: {
        statusOnEdit(val) {
            if (!this.statusOnEdit) return;
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
    margin: 10px auto;
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

.cancel {
    color: rgb(85, 84, 84);
    border: 2px solid gray;
    margin-right: 5px;
}
</style>
