document.addEventListener('DOMContentLoaded', function () {
    // Função para alternar o menu lateral
    function setupMenuToggle() {
        const menuToggle = document.getElementById('menuToggle');
        const sidebarMenu = document.getElementById('sidebarMenu');
        const contentArea = document.getElementById('contentArea');
        const menuIcon = document.getElementById('menuIcon');
        const menuLinks = document.querySelectorAll('#menu a');

        if (menuToggle && sidebarMenu && contentArea && menuIcon) {
            let isMenuVisible = localStorage.getItem('menuVisible') === 'true';

            function updateMenuState(animate) {
                if (isMenuVisible) {
                    sidebarMenu.style.transform = 'translateX(0)';
                    contentArea.style.marginLeft = '250px';
                    menuIcon.style.filter = 'invert(1)';
                } else {
                    sidebarMenu.style.transform = 'translateX(-250px)';
                    contentArea.style.marginLeft = '0';
                    menuIcon.style.filter = 'invert(0)';
                }
            }

            function toggleMenu() {
                isMenuVisible = !isMenuVisible;
                localStorage.setItem('menuVisible', isMenuVisible);
                updateMenuState(true);
            }

            menuToggle.addEventListener('click', toggleMenu);

            menuLinks.forEach(link => {
                link.addEventListener('click', function (event) {
                    if (link.href === window.location.href) {
                        event.preventDefault();
                    }
                });
            });

            updateMenuState(false);
        }
    }

    // Função para confirmar o envio de formulários com modais
    function setupFormConfirmation(formId, confirmButtonId) {
        const confirmButton = document.getElementById(confirmButtonId);
        const form = document.getElementById(formId);

        if (confirmButton && form) {
            confirmButton.addEventListener('click', function () {
                form.submit();  // Submete o formulário
            });
        }
    }

    // Função para ocultar alertas automaticamente após um tempo
    function setupAutoHideAlert() {
        const alertBox = document.querySelector('.alert');
        if (alertBox) {
            setTimeout(function () {
                alertBox.style.display = 'none';  // Esconde o alerta após 3 segundos
            }, 3000);
        }
    }

    // Configurações de formulários com confirmação
    setupFormConfirmation('formCadastrarCategoria', 'confirmarCadastroCategoria');
    setupFormConfirmation('formEditarCategoria', 'confirmarEdicaoCategoria');  // Adicionado para edição
    setupFormConfirmation('formCadastrarCliente', 'confirmarCadastroCliente');
    setupFormConfirmation('formCadastrarProduto', 'confirmarCadastroProduto');
    setupFormConfirmation('formCadastrarPedido', 'confirmarCadastroPedido');

    setupFormConfirmation('formEditarCategoria', 'confirmarEdicaoCategoria');
    setupFormConfirmation('formEditarProduto', 'confirmarEdicaoProduto')
    setupFormConfirmation('formEditarCliente','confirmarEdicaoCliente')

    // Ocultar alertas automaticamente
    setupAutoHideAlert();

    // Inicializar o menu
    setupMenuToggle();
});
