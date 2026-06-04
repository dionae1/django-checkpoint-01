const btnEnviadas = document.getElementById('btn-enviadas');
const btnRecebidas = document.getElementById('btn-recebidas');
const solicitacoesEnviadas = document.getElementById('solicitacoes_enviadas');
const solicitacoesRecebidas = document.getElementById('solicitacoes_recebidas');

btnEnviadas.addEventListener('click', function () {
    solicitacoesEnviadas.classList.remove('d-none');
    solicitacoesRecebidas.classList.add('d-none');
    toggleButtonsClasses(btnEnviadas, btnRecebidas);
});

btnRecebidas.addEventListener('click', function () {
    solicitacoesEnviadas.classList.add('d-none');
    solicitacoesRecebidas.classList.remove('d-none');
    toggleButtonsClasses(btnRecebidas, btnEnviadas);
});

function toggleButtonsClasses(btnToActivate, btnToDeactivate) {
    btnToActivate.classList.add('btn-dark');
    btnToActivate.classList.remove('btn-outline-dark');
    btnToActivate.disabled = true;
    btnToDeactivate.classList.add('btn-outline-dark');
    btnToDeactivate.classList.remove('btn-dark');
    btnToDeactivate.disabled = false;
}