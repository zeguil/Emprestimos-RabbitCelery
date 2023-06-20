<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="../assets/images/icon.png" alt="Logo da Empresa" />
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
        await axios.post("http://localhost:8000/propostas/", formData);
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

<style>
body {
  background-color: #444442;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
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
  max-width: 650px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 60px);
}

h1 {
  font-family: "Poppins", sans-serif, "arial";
  font-weight: 600;
  font-size: 30px;
  color: white;
  text-align: center;
}

.row {
  margin-bottom: 25px;
}

.campo-estilizado {
  float: left;
  width: 293px;
  margin: 1rem 0;
  position: relative;
  border-radius: 4px;
}

.campo-estilizado label {
  color: #999;
  padding: 1.3rem 30px 1rem 30px;
  position: absolute;
  top: 10px;
  left: 0;
  transition: all 0.25s ease;
  pointer-events: none;
}

.campo-estilizado.largo {
  width: 650px;
  max-width: 100%;
}

input[type="text"] {
  padding: 30px;
  border: 0;
  width: 100%;
  font-size: 1rem;
  background-color: #2d2d2d;
  color: white;
  border-radius: 4px;
  outline: 0;
}

.botao-enviar {
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

.botao-enviar:hover {
  transform: translateY(3px);
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.1), 0 1px 1px 0 rgba(0, 0, 0, 0.09);
  background-color: #3a77d7;
}

.campo-estilizado input:focus ~ label,
.campo-estilizado input:valid ~ label {
  font-size: 0.75em;
  color: #999;
  top: -10px;
  transition: all 0.225s ease;
}

@media only screen and (max-width: 768px) {
  .campo-estilizado {
    width: 100%;
  }

  .botao-enviar {
    width: 100%;
    float: none;
    text-align: center;
  }
}
</style>
