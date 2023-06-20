<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="./icon.png" alt="Logo da Empresa" />
      <h1 class="company-name">SIMPLE BANK</h1>
    </div>
  </nav>
  <div class="container">
    <div class="row">
      <h1>COMPLETE OS CAMPOS ABAIXO!</h1>
    </div>
    <div class="row input-container">
      <div class="col-xs-12">
        <div class="campo-estilizado largo">
          <input
            v-model="nomeCompleto"
            type="text"
            id="nomeCompleto"
            required
            maxlength="80"
          />
          <label>Nome Completo</label>
        </div>
      </div>
      <div class="col-md-6 col-sm-12">
        <div class="campo-estilizado">
          <input v-model="cpf" type="text" id="cpf" required />
          <label>CPF</label>
        </div>
      </div>
      <div class="col-md-6 col-sm-12">
        <div class="campo-estilizado" style="float: right">
          <input
            v-model="valorEmprestimo"
            type="text"
            id="valorEmprestimo"
            required
          />
          <label>Valor do Empréstimo</label>
        </div>
      </div>
      <div class="col-xs-12">
        <div class="campo-estilizado largo">
          <input
            v-model="endereco"
            type="text"
            id="endereco"
            required
            maxlength="80"
          />
          <label>Endereço</label>
        </div>
      </div>
      <div class="col-xs-12">
        <div class="botao-enviar" @click="enviarFormulario">Enviar</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      nomeCompleto: "",
      cpf: "",
      endereco: "",
      valorEmprestimo: "",
    };
  },
  methods: {
    async enviarFormulario() {
      const formData = {
        nome_completo: this.nomeCompleto,
        cpf: this.cpf.replace(/\D/g, ""),
        endereco: this.endereco,
        valor_emprestimo: this.valorEmprestimo.replace(",", "."),
      };

      try {
        await axios.post("http://localhost:8000/propostas", formData);
        this.$router.push({ name: "Confirm" });
      } catch (error) {
        console.error("Erro ao enviar o formulário:", error);
        this.$router.push({ name: "Confirm" });
      }
    },
  },
  mounted() {
    const cpfInput = document.getElementById("cpf");
    const nomeCompletoInput = document.getElementById("nomeCompleto");
    const enderecoInput = document.getElementById("endereco");
    const valorEmprestimoInput = document.getElementById("valorEmprestimo");

    valorEmprestimoInput.addEventListener("input", function () {
      let valor = valorEmprestimoInput.value.replace(/\D/g, "");
      valor = valor.slice(0, 8);
      valor = valor.replace(/(\d{1,})(\d{2})$/, "$1,$2");
      valorEmprestimoInput.value = valor;
    });

    cpfInput.addEventListener("input", function () {
      const cpf = cpfInput.value.replace(/\D/g, "");
      const cpfFormatted = formatCPF(cpf);
      cpfInput.value = cpfFormatted;
    });

    nomeCompletoInput.addEventListener("input", function () {
      const nomeCompleto = nomeCompletoInput.value.substring(0, 80);
      nomeCompletoInput.value = nomeCompleto;
    });

    enderecoInput.addEventListener("input", function () {
      const endereco = enderecoInput.value.substring(0, 80);
      enderecoInput.value = endereco;
    });

    function formatCPF(cpf) {
      if (cpf.length < 4) {
        return cpf;
      } else if (cpf.length < 7) {
        return cpf.substring(0, 3) + "." + cpf.substring(3);
      } else if (cpf.length < 10) {
        return (
          cpf.substring(0, 3) +
          "." +
          cpf.substring(3, 6) +
          "." +
          cpf.substring(6)
        );
      } else {
        return (
          cpf.substring(0, 3) +
          "." +
          cpf.substring(3, 6) +
          "." +
          cpf.substring(6, 9) +
          "-" +
          cpf.substring(9, 11)
        );
      }
    }
  },
};
</script>

<style src="./FormPage.css"></style>
