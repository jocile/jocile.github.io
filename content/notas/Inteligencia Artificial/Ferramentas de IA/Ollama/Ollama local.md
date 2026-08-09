---
title: "Ollama local"
description: "simplifica o uso de modelos de linguagem natural (LLMs) localmente, eliminando a necessidade de configurações complexas ou dependência de servidores externos."
tags:
  - Inteligencia-artificial/Ferramentas
  - Inteligencia-artificial/Ollama
---

## Executando Inteligências Artificais localmente

### O que é Ollama?

>[!summary] Ollama é uma ferramenta e plataforma que simplifica o uso de modelos de linguagem natural (LLMs) localmente, eliminando a necessidade de configurações complexas ou dependência de servidores externos. Ela permite que desenvolvedores e entusiastas de IA utilizem modelos avançados de linguagem de maneira mais acessível e eficiente, facilitando a integração e experimentação com LLMs em diversos projetos.

Esses são os comandos básicos para instalar, listar, e executar modelos de inteligência artificial com o Ollama. Ele permite rodar LLMs poderosos localmente em seu computador pelo terminal ou pelo navegador, sem depender de serviços na nuvem [^1].

Aqui estão os principais comandos do Ollama para executar modelos de linguagem:

## Instalação

Para instalar o Ollama, você pode usar o seguinte comando no Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Para o Windows use o instalador: [OllamaSetup.exe](https://ollama.com/download/OllamaSetup.exe)

## Verificar versão

Após a instalação, verifique a versão do Ollama com:

```
ollama --version
```

## Listar modelos disponíveis

Para ver quais modelos estão disponíveis para uso:

```
ollama list
```

Para conhecer os modelos disponíveis acesse : [Model library](https://ollama.com/library)

## Principais Comandos do Ollama

Execute `ollama` no terminal para exibir os comandos disponíveis:

| Comando               | descrição                                          |
| --------------------- | -------------------------------------------------- |
| `ollama help comando` | exibe informações sobre o comando                  |
| `ollama run llama3`   | executa um modelo, baixa caso não esteja instalado |
| `ollama pull llama3`  | atualiza o modelo, nesse caso o `llama3`           |
| `ollama rm llama2`    | remove o modelo, nesse caso o `lamma2`             |
| `ollama --version`    | mostra a versão atual instalada do `ollama`        |
| `ollama list`         | lista os modelos instalados                        |
| `ollama serve`        | inicia o servidor `ollama`                         |
| `ollama show`         | exibe informações de um modelo                     |
| `ollama create`       | Cria um modelo a partir de um Modelfile            |
| `ollama push`         | envia um modelo para o registry                    |
| `ollama ps`           | lista os modelos executando                        |
| `ollama cp`           | copia um modelo                                    |

## Executar modelos

Para executar um modelo específico, use o comando run seguido pelo nome do modelo:

```
ollama run llama3
```

Este comando inicia o modelo Llama3 de 8B parâmetros. Você pode então interagir com o modelo usando comandos como `/show`, `/show info`, etc. ^[[Descomplicando Ollama Parte-1](https://www.linuxtips.io/blog/descomplicando-ollama-parte-1)] ^[ [Ollama - Guia Rápido de Instalação e Utilização com o Llama3 e Mistral](https://pt.linkedin.com/pulse/ollama-guia-r%C3%A1pido-de-instala%C3%A7%C3%A3o-e-utiliza%C3%A7%C3%A3o-com-o-marcos-henrique-s7mbf)] ^[[100SECURITY](https://www.100security.com.br/ollama)]

Para modelos como Mistral, primeiro baixe o modelo em formato GGUF, crie um arquivo Modelfile com a linha:

```
FROM ./nome_do_arquivo_GGUF.gguf
```

E então execute:

```
ollama create Mistral -f ./Modelfile
```

Para iniciar o modelo Mistral, use ^[[Como usar LLMs localmente com ollama e Python - All Things IT @AI](https://ai.atsit.in/pt/posts/5867642908/)]:

```
ollama run Mistral
```

## Finalizar o chat com o modelo

Após iniciar um modelo, você pode interagir com ele diretamente no prompt do Ollama. Para sair, digite `/bye`.

## Usar interface gráfica

Para interagir com o Ollama além do terminal, existem várias interfaces gráficas similares ao ChatGPT usando o navegador, por exemplo a [OpenWebUI](https://docs.openwebui.com/), que cria uma página local em: <http://localhost:8080/> , este se comunica com o servidor local do Ollama, através de sua API disponibilizada por sua comunicação no seu endereço de rede local: <http://localhost:11434/>.

- A opção mais simples de interface gráfica é o [ollama-ui: Simple HTML UI para o Ollama](https://github.com/rtcfirefly/ollama-ui) - É uma interface Web para o Ollama que interage através de um plugin do Chrome.
- O [Msty - usando AI Models de maneira Simples e fácil](https://msty.app/) - é uma interface muito popular com diversos recursos de gerenciamentos de prompts.
- Outra também muito popular e com os recursos mais avançados, mas um pouco complicada para instalar é o [Open WebUI](https://docs.openwebui.com/), a forma mais prática de instalar é o usar o seu contêiner Docker, que já traz toda a configuração necessária com um único comando, mas requer o Docker instalado, para mais informações acesse: [Início rápido com Open WebUI](https://docs.openwebui.com/getting-started/).

## Referências

- [GitHub - ollama/ollama: Get up and running with Llama 3, Mistral, Gemma 2, and other large language models.](https://github.com/ollama/ollama)
- [Ollama.com](https://ollama.com/)
- [Descomplicando Ollama Parte-1](https://www.linuxtips.io/blog/descomplicando-ollama-parte-1)
- [Ollama - Guia Rápido de Instalação e Utilização com o Llama3 e Mistral](https://pt.linkedin.com/pulse/ollama-guia-r%C3%A1pido-de-instala%C3%A7%C3%A3o-e-utiliza%C3%A7%C3%A3o-com-o-marcos-henrique-s7mbf)
- [100SECURITY](https://www.100security.com.br/ollama)
- [Como usar LLMs localmente com ollama e Python - All Things IT @AI](https://ai.atsit.in/pt/posts/5867642908/)
- [INTELIGÊNCIA ARTIFICIAL - COMO USAR O OLLAMA PARA TESTAR VÁRIOS MODELOS DE IA ! - YouTube](https://www.youtube.com/watch?v=GEwsz93VlEo)
- [ollama/docs/faq.md at main · ollama/ollama · GitHub](https://github.com/ollama/ollama/blob/main/docs/faq.md)
- [Getting started with Meta Llama | Documentation](https://llama.meta.com/docs/get-started/)
- [ Interface gráfica para o ollama - Open WebUI](https://docs.openwebui.com/)
- [How to prompt Code Llama · Ollama Blog](https://ollama.com/blog/how-to-prompt-code-llama)
- [Rodando Modelos de Linguagem Natural Localmente com Ollama | Asimov Academy](https://hub.asimov.academy/tutorial/rodando-modelos-de-linguagem-natural-localmente-com-ollama/)

[^1]: [Site de segurança da informação - 100SECURITY](https://www.100security.com.br/ollama)
