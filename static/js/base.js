document.addEventListener('DOMContentLoaded', function () {
    
    // Função para alternar o estado do menu lateral
    function setupMenuToggle() {
        const menuToggle = document.getElementById('menuToggle');
        const sidebarMenu = document.getElementById('sidebarMenu');
        const contentArea = document.getElementById('contentArea');
        const menuIcon = document.getElementById('menuIcon');
        const menuLinks = document.querySelectorAll('#menu a');

        if (menuToggle && sidebarMenu && contentArea && menuIcon) {
            let isMenuVisible = getMenuStateFromStorage();

            function getMenuStateFromStorage() {
                return localStorage.getItem('menuVisible') === 'true';
            }

            function updateMenuState(withAnimation) {
                const transitionValue = withAnimation ? 'transform 0.3s ease, margin-left 0.3s ease' : 'none';
                sidebarMenu.style.transition = transitionValue;
                contentArea.style.transition = transitionValue;

                if (isMenuVisible) {
                    openMenu();
                } else {
                    closeMenu();
                }
            }

            function openMenu() {
                sidebarMenu.style.transform = 'translateX(0)';
                contentArea.style.marginLeft = '250px';
                menuIcon.style.filter = 'invert(1)'; // Ícone branco
            }

            function closeMenu() {
                sidebarMenu.style.transform = 'translateX(-250px)';
                contentArea.style.marginLeft = '0';
                menuIcon.style.filter = 'invert(0)'; // Ícone cinza escuro
            }

            function toggleMenu() {
                isMenuVisible = !isMenuVisible;
                localStorage.setItem('menuVisible', isMenuVisible);
                updateMenuState(true);
            }

            function preventPageReloadOnActiveLink(link, event) {
                if (link.href === window.location.href) {
                    event.preventDefault();
                }
            }

            // Inicializa o estado do menu ao carregar a página
            updateMenuState(false);

            // Alterna o estado do menu ao clicar no ícone de hambúrguer
            menuToggle.addEventListener('click', toggleMenu);

            // Previne o recarregamento da página ao clicar na rota ativa
            menuLinks.forEach(link => {
                link.addEventListener('click', function (event) {
                    preventPageReloadOnActiveLink(link, event);
                });
            });
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

    // Inicializa as funcionalidades
    setupMenuToggle();
    setupFormConfirmation('formEditarCategoria', 'confirmarEdicao'); // Confirmação para editar categoria
    setupFormConfirmation('formCadastrarCategoria', 'confirmarCadastro'); // Confirmação para cadastrar categoria
    setupAutoHideAlert(); // Ocultar alertas automaticamente
});
