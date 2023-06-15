<template>
  <div class="form-page">
    <div class="content">
      <h1>Preencha o formulário</h1>
      <form @submit="submitForm">
        <div class="form-group">
          <label for="nome_completo">Nome Completo</label>
          <input type="text" id="nome_completo" v-model="nomeCompleto" required>
        </div>
        <div class="form-group">
          <label for="cpf">CPF</label>
          <input type="text" id="cpf" v-model="cpf" required>
        </div>
        <div class="form-group">
          <label for="endereco">Endereço</label>
          <input type="text" id="endereco" v-model="endereco" required>
        </div>
        <div class="form-group">
          <label for="valor_emprestimo">Valor do Empréstimo</label>
          <input type="number" id="valor_emprestimo" v-model="valorEmprestimo" required>
        </div>
        <button type="submit">Enviar</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nomeCompleto: '',
      cpf: '',
      endereco: '',
      valorEmprestimo: null,
    };
  },
  methods: {
    submitForm() {
      // Aqui você pode enviar os dados do formulário para http://127.0.0.1:8000/propostas/
      // Use uma biblioteca como Axios para fazer a requisição HTTP
      console.log('Enviando formulário:', this.nomeCompleto, this.cpf, this.endereco, this.valorEmprestimo);
    },
  },
  mounted() {
    document.body.style.backgroundImage = "url('https://img.freepik.com/premium-vector/financial-banking-technology-concept_387612-31.jpg')";
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundPosition = "center";
  },
};
</script>

<style scoped>
.form-page {
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

.form-group {
  margin-bottom: 16px;
}

label {
  display: block;
}

input {
  width: 100%;
  padding: 8px;
}

button {
  margin-top: 16px;
}
</style>
