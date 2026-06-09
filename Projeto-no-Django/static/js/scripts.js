const paginas = {
    'adm_home': "administrador/"
}

function navegar(rota) {
    const pagina = paginas[rota]
    if (!pagina) return;
    window.location.href === pagina
}