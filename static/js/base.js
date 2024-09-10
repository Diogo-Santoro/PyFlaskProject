document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menuToggle');
    const sidebarMenu = document.getElementById('sidebarMenu');
    const contentArea = document.getElementById('contentArea');
    const menuIcon = document.getElementById('menuIcon');
    const menuLinks = document.querySelectorAll('#menu a'); // Seleciona todos os links do menu

    // Inicializa o estado do menu com base no localStorage
    let isMenuVisible = getMenuStateFromStorage();

    /**
     * Função: Recupera o estado do menu do localStorage
     * Retorna: 'true' ou 'false' dependendo se o menu estava aberto ou fechado
     */
    function getMenuStateFromStorage() {
        return localStorage.getItem('menuVisible') === 'true';
    }

    /**
     * Função: Define o estado do menu (aberto/fechado) com ou sem animação
     * Parâmetro: withAnimation - booleano, true para aplicar animação, false para desativá-la
     */
    function updateMenuState(withAnimation) {
        // Controla se a transição será ativada ou desativada
        const transitionValue = withAnimation ? 'transform 0.3s ease, margin-left 0.3s ease' : 'none';
        sidebarMenu.style.transition = transitionValue;
        contentArea.style.transition = transitionValue;

        // Atualiza a interface com base no estado do menu
        if (isMenuVisible) {
            openMenu();
        } else {
            closeMenu();
        }
    }

    /**
     * Função: Abre o menu e ajusta a interface
     */
    function openMenu() {
        sidebarMenu.style.transform = 'translateX(0)';
        contentArea.style.marginLeft = '250px';
        menuIcon.style.filter = 'invert(1)'; // Ícone branco
    }

    /**
     * Função: Fecha o menu e ajusta a interface
     */
    function closeMenu() {
        sidebarMenu.style.transform = 'translateX(-250px)';
        contentArea.style.marginLeft = '0';
        menuIcon.style.filter = 'invert(0)'; // Ícone cinza escuro
    }

    /**
     * Função: Alterna o estado do menu e salva no localStorage
     */
    function toggleMenu() {
        isMenuVisible = !isMenuVisible;
        localStorage.setItem('menuVisible', isMenuVisible); // Salva o estado
        updateMenuState(true); // Aplica o novo estado com animação
    }

    /**
     * Função: Previne o recarregamento da página se o link clicado já estiver ativo
     * Parâmetro: link - O elemento de link (anchor) clicado
     */
    function preventPageReloadOnActiveLink(link) {
        if (link.href === window.location.href) {
            event.preventDefault();
        }
    }

    // Aplica o estado do menu sem animação ao carregar a página
    updateMenuState(false);

    // Alterna o estado do menu ao clicar no ícone de hambúrguer
    menuToggle.addEventListener('click', toggleMenu);

    // Previne o recarregamento da página ao clicar na rota ativa
    menuLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            preventPageReloadOnActiveLink(link);
        });
    });
    
    // Modal de confirmação após cadastrar categoria
    document.addEventListener('DOMContentLoaded', function() {
    const formCadastrarCategoria = document.getElementById('formCadastrarCategoria');

        formCadastrarCategoria.addEventListener('submit', function(event) {
            event.preventDefault();

            // Lógica para cadastrar a categoria via AJAX, se necessário, ou apenas mostrar o modal
            const modal = new bootstrap.Modal(document.getElementById('confirmationModal'));
            modal.show();

            // Aqui você pode adicionar lógica de envio do formulário via AJAX, se desejar
        });
    });


});
