const axios = require('axios');

async function makePostRequest() {
  try {
    const formData = {
      nome_completo: 'Maria do Carmo',
      cpf: '11122233349',
      endereco: 'Rua 2',
      valor_emprestimo: 15000,
    };

    const response = await axios.post('http://localhost:8000/propostas', formData);

    console.log('Resposta do servidor:', response.data);
  } catch (error) {
    console.error('Erro na requisição:', error);
  }
}

makePostRequest();
