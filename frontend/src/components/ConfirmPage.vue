<template>
  <div>
    <nav class="navbar">
      <div class="navbar-logo">
        <img src="./icon.png" alt="Logo da Empresa" />
        <h1 class="company-name">SIMPLE BANK</h1>
      </div>
    </nav>
    <div class="container">
      <div class="row">
        <h1>PROPOSTA ENVIADA.</h1>
        <div class="box">
          <p>
            Parabéns! Sua proposta foi enviada com sucesso. Agora, nossa equipe
            de especialistas irá analisá-la cuidadosamente. Agradecemos sua
            paciência enquanto avaliamos todas as informações fornecidas.
            <br /><br>

            Fique tranquilo(a), faremos o possível para agilizar o processo de
            análise. Você pode esperar uma resposta definitiva em até 48 horas.
            Durante esse período, estaremos dedicados a avaliar todas as
            informações e tomar a melhor decisão para atender às suas
            necessidades.
            <br /><br />
            Agradecemos sua confiança em nossa empresa e estamos ansiosos para
            oferecer uma resposta o mais breve possível. Caso tenha alguma
            dúvida adicional, sinta-se à vontade para entrar em contato conosco.
            Estamos aqui para ajudar.
          </p>
        </div>
        <button class="button" @click="redirectToHome">voltar</button>
      </div>
    </div>
  </div>
</template>

<style>
body {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  overflow: hidden;
  background-color: #444442;
}

.navbar {
  background-color: #2d2d2d;
  color: white;
  display: flex;
  align-items: center;
  padding: 1px 10px;
  width: 100vw;
  height: 50px;
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

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Definir a altura como 100vh */
  margin-top: -100px;
  width: 100%;
  max-width: 600px;
}
.box {
  padding: 20px;
  border: 0;
  width: 80%;
  max-width: 600px;
  font-size: 1rem;
  background-color: #2d2d2d;
  color: white;
  border-radius: 4px;
  outline: 0;
  margin: 0 auto;
}

h1 {
  color: white;
}

.row {
  text-align: center;
}

.button {
  margin-top: 20px;
  padding: 7px 35px;
  border-radius: 60px;
  display: inline-block;
  background-color: #4b8cfb;
  color: white;
  font-size: 18px;
  cursor: pointer;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.06), 0 2px 10px 0 rgba(0, 0, 0, 0.07);
  transition: all 300ms ease;
}

.button:hover {
  transform: translateY(3px);
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.1), 0 1px 1px 0 rgba(0, 0, 0, 0.09);
  background-color: #3a77d7;
}
</style>
<script>
export default {
  methods: {
    redirectToHome() {
      this.$router.push("/");
    },
  },
};
</script>
