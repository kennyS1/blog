<template>
  <Navbar />
  <div class="card">
    <div class="card-body">
      FastAPI
    </div>
  </div>

</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
  data() {
    return {
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
.tabs {
  margin-bottom: 20px;
}
button {
  padding: 10px 20px;
  margin-right: 10px;
  border: none;
  cursor: pointer;
}
button.active {
  background-color: #42b983;
  color: white;
}
</style>