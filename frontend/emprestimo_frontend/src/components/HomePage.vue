<template>
  <div class="home-page">
    <div class="content">
      <h1>FAÇA SEU EMPRÉSTIMO</h1>
      <button @click="redirectToForm">Clique aqui</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    redirectToForm() {
      this.$router.push('/form');
    },
  },
  mounted() {
    document.body.style.backgroundImage = "url('https://i.pinimg.com/736x/15/3a/45/153a4535df6cf2d2b106a558b750c486.jpg')";
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundPosition = "center";
  },
};
</script>

<style scoped>
.home-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.content {
  text-align: center;
}

h1 {
  font-size: 24px;
}

button {
  margin-top: 16px;
}
</style>
