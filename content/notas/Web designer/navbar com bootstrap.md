---
title: Navbar Com Bootstrap
description: fazer uma barra lateral
date: '2026-08-12'
draft: false
tags:
- Webdesign
- Bootstrap
---

Para fazer uma barra lateral (sidebar) com Bootstrap, você pode ==usar uma combinação do componente de Grade (para dividir a página em colunas) e do componente de Colapso para criar a interatividade de abrir e fechar a barra==. Outra opção é o componente Offcanvas, que cria uma barra lateral que surge por sobre o conteúdo, sendo ideal para dispositivos móveis ou para um efeito de overlay. 

Usando Grade e Colapso (Push-style Sidebar)

Este método cria uma barra lateral que "empurra" o conteúdo principal, em vez de cobri-lo. 

1. **Estruture a página com o Grid System do Bootstrap:**
 - Crie um container e uma linha (row) dentro dele.
 - Dentro da linha, crie duas colunas: uma para a barra lateral (por exemplo, `col-md-3`) e outra para o conteúdo principal (por exemplo, `col-md-9`).

Código

```html
<div class="container-fluid">
 <div class="row">
 <!-- Coluna da Sidebar -->
 <div class="col-md-3 bg-light sidebar">
 <!-- Conteúdo da sua barra lateral -->
 <ul class="nav flex-column">
 <li class="nav-item">
 <a class="nav-link" href="#">Link 1</a>
 </li>
 <li class="nav-item">
 <a class="nav-link" href="#">Link 2</a> </li>
 </ul>
 </div> <!-- Conteúdo Principal -->
 <div class="col-md-9 main-content">
 <!-- Seu conteúdo aqui -->
 </div>
 </div>
</div>
```

1. **Adicione um botão para abrir/fechar e o componente Collapse:**
 - Crie um botão que terá como alvo o `div` da barra lateral usando `data-bs-toggle="collapse"` e `data-bs-target=""`. 
 - Adicione o `id="sidebarCollapse"` ao `div` da barra lateral e a classe `collapse`. 

Código

```html
<!-- Botão para abrir/fechar -->
<button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target=""
 aria-expanded="false" aria-controls="sidebarCollapse"> Menu </button>
 <!-- A sua barra lateral vai aqui -->
<div class="col-md-3 sidebar collapse" id="sidebarCollapse">
 <!--... conteúdo da sidebar... -->
</div>
```

Usando o Componente Offcanvas (Overlay-style Sidebar)

Este é um componente mais moderno que desliza da borda da tela, cobrindo parte do conteúdo. 

1. **1.** **Crie um botão que aciona o Offcanvas:**
 
 - Use um botão com os atributos `data-bs-toggle="offcanvas"` e `data-bs-target=""`.
 
2. **2.** **Crie o componente Offcanvas:**
 
 - Crie um `div` com a classe `offcanvas` e um `id` que corresponda ao alvo do botão (``).
 - Adicione classes como `offcanvas-start` para posicionar a barra lateral no início da tela (esquerda).
 

Código

```html
<!-- Botão para abrir o Offcanvas -->
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target=""
 aria-controls="offcanvasExample"> Abrir Offcanvas </button> <!-- O Offcanvas -->
<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
 <div class="offcanvas-header">
 <h5 class="offcanvas-title" id="offcanvasExampleLabel">Barra Lateral</h5> <button type="button" class="btn-close"
 data-bs-dismiss="offcanvas" aria-label="Close"></button>
 </div>
 <div class="offcanvas-body">
 <div> Algum texto e links aqui. </div> <!-- Outro conteúdo da barra lateral -->
 </div>
</div>
```

## Referências

- [Bootstrap 5 Sidebar Examples - DEV Community](https://dev.to/codeply/bootstrap-5-sidebar-examples-38pb)
- [Navbar · Bootstrap em Português](https://getbootstrap.com.br/docs/4.1/components/navbar/)
- [Bootstrap 5 Navigation Bars](https://www.w3schools.com/bootstrap5/bootstrap_navbar.php)
