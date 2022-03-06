import {createStore} from 'vuex'

const store = createStore({
  state() {
    return {
      count: 0,
      todos: [
        { id: 1, text: 'id1', done: true },
        { id: 2, text: 'id2', done: false },
        { id: 3, text: 'id3', done: true },
        { id: 4, text: 'id4', done: false },
        { id: 5, text: 'id5', done: false },
      ]
    }
  },
  mutations: {
    increment(state) {
      state.count++
    },
    double(state) {
      state.count = state.count * 2
    }
  },
  getters: {
    doneTodos: (state) => {
      return state.todos.filter(todo => todo.done)
    }
  }
})

export default store
