function limpa_formulario_cep() {
    //Limpa valores do formulário de cep.
    document.getElementById('adress').value=("");
    document.getElementById('district').value=("");
    document.getElementById('city').value=("");
    document.getElementById('state').value=("");
}

function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('adress').value=(conteudo.logradouro);
        document.getElementById('district').value=(conteudo.bairro);
        document.getElementById('city').value=(conteudo.localidade);
        document.getElementById('state').value=(conteudo.uf);
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulario_cep();
        alert("CEP não encontrado.");
        document.getElementById('cep').value=("");
    }
}
    
function pesquisacep(valor) {

    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep !== "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if(validacep.test(cep)) {

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('adress').value="...";
            document.getElementById('district').value="...";
            document.getElementById('city').value="...";
            document.getElementById('state').value="...";

            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = '//viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //cep é inválido.
            limpa_formulario_cep();
            alert("Formato de CEP inválido.");
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulario_cep();
    }
}

function formatar(mascara, documento){
    var i = documento.value.length;
    var saida = mascara.substring(0,1);
    var texto = mascara.substring(i);

    if (texto.substring(0,1) != saida){
        documento.value += texto.substring(0,1);
    }
}

function exibe(i) {
    document.getElementById(i).readOnly= true;
}

function desabilita(i){
    document.getElementById(i).disabled = true;    
}

function habilita(i){
    document.getElementById(i).disabled = false;
}


function showhide() {
   var div = document.getElementById("newpost");
   if(idade()>=18){
        div.style.display = "none";
   }   
   else if(idade()<18) {
        div.style.display = "inline";
    }
}