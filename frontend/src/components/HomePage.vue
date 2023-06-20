<template>
  <div>
    <nav class="navbar">
      <div class="navbar-logo">
        <img src="../assets/images/icon.png" alt="Logo da Empresa" />
        <h1 class="company-name">SIMPLE BANK</h1>
      </div>
      <ul class="navbar-links">
        <li><a href="https://linkbee.me/FbOmiVvcbO">contato</a></li>
      </ul>
    </nav>
    <div class="background-image">
      <div class="content-wrapper">
        <div class="left-content">
          <div class="vertical-div"></div>
          <div class="vertical-div2">
            <h1 class="title">FAÇA SEU EMPRÉSTIMO!</h1>
            <p class="slogan">
              Seu futuro começa agora! Descubra o poder do nosso banco para
              realizar seus sonhos com nossos empréstimos flexíveis.
            </p>
            <button class="button" @click="redirectToFormPage">
              Clique Aqui
            </button>
          </div>
          <div class="vertical-div"></div>
        </div>
        <div class="right-content"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    redirectToFormPage() {
      this.$router.push("/form");
    },
  },
};
</script>
<style>
h1 {
  color: #ffffff;
  font-size: 24px;
  margin-bottom: 10px;
}

p {
  color: #ffffff;
  font-size: 18px;
  margin-bottom: 10px;
}

body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.navbar {
  background-color: black;
  color: white;
  display: flex;
  align-items: center;
  padding: 1px;
}

.navbar:hover {
  transform: scale(1);
}

.navbar-logo {
  display: flex;
  align-items: center;
  margin-left: 20px;
}

.navbar-logo img {
  height: 25px;
  margin-right: 10px;
  filter: brightness(120%);
  transition: filter 0.3s;
}

.navbar-logo:hover img {
  filter: brightness(150%);
}

.company-name {
  font-size: 20px;
  margin: 0;
  font-family: "Kanit", sans-serif;
  display: flex;
  align-items: center;
  transition: font-size 0.3s, text-shadow 0.3s;
}

.company-name:hover {
  font-size: 22px;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

.navbar-links {
  margin-left: auto;
  margin-right: 80px;
  list-style: none;
  display: flex;
  font-family: "Kanit", sans-serif;
}

.navbar-links li {
  margin-left: 20px;
}

.navbar-links li a {
  transition: font-size 0.3s, text-shadow 0.3s;
  color: white;
  text-decoration: none;
  transition: transform 0.3s;
}

.navbar-links li a:hover {
  font-size: 16.1px;
  transform: scale(1.1);

  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

.background-image {
  position: relative;
  width: 100%;
  height: calc(100vh - 50px);
  overflow: hidden;
}

.background-image::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  background-image: url("../assets/images/bank.jpg");
  width: 100%;
  height: 170%;
  background-size: cover;
  background-position: center;
  filter: brightness(30%);

  z-index: -1;
  border: none;
  outline: none;
  box-shadow: none;
}

.content-wrapper {
  display: flex;
  height: 100%;
}

.left-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
  margin-left: 60px;
}

.right-content {
  flex: 1;
}

.vertical-div {
  flex: 1;
  margin: 10px;
}

.vertical-div2 {
  flex: 1;
  margin: 10px;
}

.title {
  font-size: 40px;
  text-shadow: 2px 3px rgba(0, 0, 0, 0.5);
  font-family: "Kanit", sans-serif;
}

.slogan {
  font-size: 25px;
  text-shadow: 2px 3px rgba(0, 0, 0, 0.5);
  font-family: "Arial", sans-serif;
}

.button {
  padding: 10px 20px;
  color: white;
  border: none;
  font-size: 16px;
  cursor: pointer;
  margin-top: 15px;
  border-color: #4184f8;
  color: #fff;
  background-color: #4184f8;
  -webkit-transition: all 0.35s;
  -moz-transition: all 0.35s;
  transition: all 0.35s;
  border-radius: 300px;
  text-transform: uppercase;
}

.button:hover {
  border-color: black;
  color: #fff;
  background-color: #1564e4;
  transform: translateY(2px);
}
</style>
