let janelaAtual = null;

function navegar(evento) {
    document.querySelectorAll('.navegacao').forEach(b => b.classList.remove('atual'));
    const alvo = evento.currentTarget;
    alvo.classList.add('atual');
    const texto = alvo.textContent;
    let categoria = '';
    if (texto.includes('Administrador')) categoria = 'administrador';
    else if (texto.includes('Cliente')) categoria = 'cliente';
    else if (texto.includes('Produto')) categoria = 'produto';
    else if (texto.includes('Carrinho')) categoria = 'carrinho';
    
    carregarDados(categoria);
}

async function carregarDados(categoria) {
    const resposta = await API.request(`/${categoria}/`);
    if (resposta.sucesso) {
        criarTabela(categoria, resposta.dados);
    } else {
        mensagem(resposta.mensagem);
    }
}

function criarTabela(categoria, dados) {
    const div = document.getElementById('div');
    div.innerHTML = '';
    
    const h1 = document.createElement('h1');
    h1.textContent = categoria.charAt(0).toUpperCase() + categoria.slice(1);
    div.appendChild(h1);
    
    const btnCriar = document.createElement('button');
    btnCriar.textContent = 'Criar';
    btnCriar.onclick = () => abrirFormulario(categoria);
    div.appendChild(btnCriar);
    
    if (dados.length === 0) {
        const msg = document.createElement('p');
        msg.textContent = `Nenhum ${categoria} encontrado`;
        div.appendChild(msg);
        return;
    }
    
    document.createElement('br');
    const tabela = document.createElement('table');
    tabela.style.cssText = 'border: 1px solid';
    const thead = document.createElement('thead');
    const tr = document.createElement('tr');
    
    ['ID', 'Nome', 'Ações'].forEach(texto => {
        const th = document.createElement('th');
        th.textContent = texto;
        tr.appendChild(th);
    });
    
    thead.appendChild(tr);
    tabela.appendChild(thead);
    
    const tbody = document.createElement('tbody');
    dados.forEach(item => {
        const tr = document.createElement('tr');
        
        const tdId = document.createElement('td');
        tdId.textContent = item.id;
        tdId.style.cssText = 'padding: 15px;';
        tr.appendChild(tdId);
        
        const tdNome = document.createElement('td');
        if (categoria === 'carrinho') {
            tdNome.textContent = item.cliente_nome;
        } else {
            tdNome.textContent = item.nome;
        }
        tdNome.style.cssText = 'padding: 15px;';
        tr.appendChild(tdNome);
        
        const tdAcoes = document.createElement('td');
        tdAcoes.style.cssText = 'padding: 15px;';
        
        if (categoria === 'carrinho') {
            const btnVer = document.createElement('button');
            btnVer.textContent = 'Ver';
            btnVer.type = 'button';
            btnVer.onclick = () => verCarrinho(item.id);
            tdAcoes.appendChild(btnVer);
        }
        
        const btnEdit = document.createElement('button');
        btnEdit.textContent = 'Editar';
        btnEdit.type = 'button';
        btnEdit.onclick = () => abrirFormulario(categoria, item.id);
        
        const btnDel = document.createElement('button');
        btnDel.textContent = 'Deletar';
        btnDel.type = 'button';
        btnDel.onclick = () => deletar(categoria, item.id);
        
        tdAcoes.appendChild(btnEdit);
        tdAcoes.appendChild(btnDel);
        
        tr.appendChild(tdAcoes);
        tbody.appendChild(tr);
    });
    
    tabela.appendChild(tbody);
    div.appendChild(tabela);
}


const API = {
    async request(url, method = 'GET', dados = null) {
        const requisicao = {
            method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': window.csrftoken
            }
        };

        if (dados) {
            requisicao.body = JSON.stringify(dados);
        }

        try {
            const resposta = await fetch(url, requisicao);
            const json = await resposta.json();
            return json;
        } catch (error) {
            console.error('Erro na requisição:', error);
            return { success: false, mensagem: 'Erro na requisição' };
        }
    },
};


async function abrirFormulario(categoria, id = null) {
    let opcoes = {};
    
    if (categoria === 'cliente' || categoria === 'produto') {
        const admOpcoes = await API.request('/opcoes/administrador/');
        opcoes.administrador = admOpcoes.dados || [];
    }
    if (categoria === 'carrinho') {
        const clientOpcoes = await API.request('/opcoes/cliente/');
        opcoes.cliente = clientOpcoes.dados || [];
    }
    
    const janela = criarjanela(id ? `Editar ${categoria}` : `Criar ${categoria}`);
    const form = criarFormulario(categoria, opcoes);
    
    if (id) {
        form.dataset.acao = 'editar';
        form.dataset.id = id;
        form.dataset.categoria = categoria;
    } else {
        form.dataset.acao = 'criar';
        form.dataset.categoria = categoria;
    }
    
    const btnSalvar = document.createElement('button');
    btnSalvar.type = 'button';
    btnSalvar.textContent = id ? 'Atualizar' : 'Salvar';
    btnSalvar.onclick = () => salvar(form, categoria);
    
    const btnCancelar = document.createElement('button');
    btnCancelar.type = 'button';
    btnCancelar.textContent = 'Cancelar';
    btnCancelar.onclick = fecharjanela();
    
    janela.appendChild(form);
    const div = document.createElement('div');
    div.appendChild(btnSalvar);
    div.appendChild(btnCancelar);
    janela.appendChild(div);
    
    mostrarjanela(janela);
}

async function salvar(form, categoria) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    
    const acao = form.dataset.acao;
    const url = (acao === 'editar') ? `/${categoria}/${form.dataset.id}/editar/` : `/${categoria}/criar/`;
    
    const response = await API.request(url, 'POST', data);
    if (response.sucesso) {
        mensagem(response.mensagem);
        fecharjanela();
        carregarDados(categoria);
    } else {
        mensagem(response.mensagem || JSON.stringify(response.dados));
    }
}

async function deletar(categoria, id) {
    if (confirm(`Tem certeza que deseja deletar este ${categoria}?`)) {
        const response = await API.request(`/${categoria}/${id}/deletar/`, 'DELETE');
        if (response.sucesso) {
            mensagem(response.mensagem);
            carregarDados(categoria);
        } else {
            mensagem(response.mensagem || JSON.stringify(response.dados));
        }
    }
}


async function verCarrinho(id) {
    const response = await API.request(`/carrinho/${id}/ver/`);
    if (response.sucesso) {
        const carrinho = response.dados;
        const janela = criarjanela(`Carrinho de ${carrinho.cliente_nome}`);
        
        let conteudo = '<table style="width: 100%; border-collapse: collapse;">';
        conteudo += '<thead><tr style="background: #f8f9fa;"><th style="padding: 10px; border-bottom: 1px solid #ddd; text-align: left;">Produto</th><th style="padding: 10px; border-bottom: 1px solid #ddd; text-align: left;">Preço</th><th style="padding: 10px; border-bottom: 1px solid #ddd; text-align: left;">Ação</th></tr></thead>';
        conteudo += '<tbody>';
        
        if (carrinho.produtos.length > 0) {
            carrinho.produtos.forEach(p => {
                conteudo += `<tr><td>${p.nome}</td><td">R$ ${p.preco}</td><td"><button onclick="removerProdutoCarrinho(${id}, ${p.id})">Remover</button></td></tr>`;
            });
        } else {
            conteudo += '<tr><td colspan="3">Nenhum produto no carrinho</td></tr>';
        }
        
        conteudo += `<tr><td>Total</td><td>R$ ${carrinho.total}</td><td></td></tr>`;
        conteudo += '</tbody></table>';
        
        janela.innerHTML = conteudo;
        
        const btnAdicionar = document.createElement('button');
        btnAdicionar.textContent = '+ Adicionar Produto';
        btnAdicionar.onclick = () => FormularioAddProduto(id);
        janela.appendChild(btnAdicionar);
        
        mostrarjanela(janela);
    } else {
        mensagem(response.mensagem);
    }
}

async function FormularioAddProduto(carrinhoId) {
    const produtos = await API.request('/produto/');
    const janela = criarjanela('Adicionar Produto');
    
    const select = document.createElement('select');
    select.name = 'produto_id';
    
    const optionVazia = document.createElement('option');
    optionVazia.value = '';
    optionVazia.textContent = '-- Selecione um produto --';
    select.appendChild(optionVazia);
    
    produtos.dados.forEach(p => {
        const option = document.createElement('option');
        option.value = p.id;
        option.textContent = `${p.nome} (R$ ${p.preco})`;
        select.appendChild(option);
    });
    
    const div = document.createElement('div');
    
    const label = document.createElement('label');
    label.textContent = 'Produto';
    div.appendChild(label);
    div.appendChild(select);
    
    janela.appendChild(div);
    
    const btnAdicionar = document.createElement('button');
    btnAdicionar.textContent = 'Adicionar';
    btnAdicionar.type = 'button';
    btnAdicionar.onclick = async () => {
        const produtoId = select.value;
        if (!produtoId) {
            mensagem('Selecione um produto');
            return;
        }
        
        const response = await API.request(`/carrinho/${carrinhoId}/adicionar/`, 'POST', {produto_id: parseInt(produtoId)});
        if (response.sucesso) {
            mensagem(response.mensagem);
            fecharjanela();
            verCarrinho(carrinhoId);
        } else {
            mensagem(response.mensagem);
        }
    };
    
    const btnCancelar = document.createElement('button');
    btnCancelar.textContent = 'Cancelar';
    btnCancelar.type = 'button';
    btnCancelar.onclick = fecharjanela;
    
    janela.appendChild(btnAdicionar);
    janela.appendChild(btnCancelar);
    
    mostrarjanela(janela);
}

async function removerProduto(carrinhoId, produtoId) {
    if (confirm('Remover este produto?')) {
        const response = await API.request(`/carrinho/${carrinhoId}/remover/${produtoId}/`, 'POST');
        if (response.sucesso) {
            mensagem(response.mensagem);
            verCarrinho(carrinhoId);
        } else {
            mensagem(response.mensagem || JSON.stringify(response.dados));
        }
    }
}



function criarjanela(titulo) {
    const janela = document.createElement('div');    
    const h1 = document.createElement('h1');
    h1.textContent = titulo;
    janela.appendChild(h1);
    return janela;
}

function criarFormulario(categoria, opcoes = {}) {
    const form = document.createElement('form');
    form.style.cssText = 'background: #f8f9fa;';
    
    const campos = {'administrador': [{ name: 'nome', label: 'Nome', type: 'text', required: true }], 'cliente': [{ name: 'administrador', label: 'Administrador', type: 'select', options: opcoes.administrador || [], required: true }, { name: 'nome', label: 'Nome', type: 'text', required: true }, { name: 'email', label: 'Email', type: 'email', required: true }, { name: 'senha', label: 'Senha', type: 'password', required: true }], 'produto': [{ name: 'administrador', label: 'Administrador', type: 'select', options: opcoes.administrador || [], required: true }, { name: 'nome', label: 'Nome', type: 'text', required: true }, { name: 'preco', label: 'Preço', type: 'number', step: '0.01', required: true }], 'carrinho': [{ name: 'cliente', label: 'Cliente', type: 'select', options: opcoes.cliente || [], required: true }]};
    
    const camposesp = campos[categoria] || [];
    camposesp.forEach(campo => {
        const div = document.createElement('div');
        div.style.cssText = 'display: flex; flex-direction: column;';
        
        const label = document.createElement('label');
        label.textContent = campo.label;
        div.appendChild(label);
        
        let input;
        if (campo.type === 'select') {
            input = document.createElement('select');
            input.name = campo.name;
            input.required = campo.required;
            
            const optionVazia = document.createElement('option');
            optionVazia.value = '';
            optionVazia.textContent = '-- Selecione --';
            input.appendChild(optionVazia);
            
            campo.options.forEach(opt => {
                const option = document.createElement('option');
                option.value = opt.id;
                option.textContent = opt.nome;
                input.appendChild(option);
            });
        } else {
            input = document.createElement('input');
            input.type = campo.type;
            input.name = campo.name;
            if (campo.step) input.step = campo.step;
            if (campo.required) input.required = true;
            input.placeholder = `Digite o(a) ${campo.label.toLowerCase()}`;
        }
        
        div.appendChild(input);
        form.appendChild(div);
    });
    
    return form;
}


function mostrarjanela(janela) {
    const overlay = document.createElement('div');
    overlay.id = 'janela-overlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9998;
        overflow-y: auto;
    `;
    overlay.onclick = (event) => {
    if (event.target === overlay) {
        fecharjanela();
    }
};
    
    overlay.appendChild(janela);
    document.body.appendChild(overlay);
    janelaAtual = overlay;
}

function fecharjanela() {
    if (janelaAtual) {
        janelaAtual.remove();
        janelaAtual = null;
    }
}

function mensagem(mensagem) {
    alert(mensagem);
}


