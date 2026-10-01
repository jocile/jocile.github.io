---
title: Análise de requisitos
description: entendermos exatamente o que o cliente precisa e deseja para o sistema
date: '2026-10-01'
draft: false
aliases:
- Requisitos
- Projeto 
---

O levantamento de requisitos é a fase inicial do desenvolvimento de software e uma das etapas mais importantes. Basicamente, é entendermos exatamente o que o cliente precisa e deseja para o sistema. Ele pode querer funcionalidades específicas ou até mesmo levar em conta regras de negócio que já existem.

---

## Importância

O principal objetivo do levantamento de requisitos é garantir que tanto os clientes quanto os desenvolvedores tenham a mesma visão do projeto. Isso evita desentendimentos e garante que o software final será realmente útil.

Além disso, esse processo nos traz benefícios como:

- Identificar as necessidades reais dos usuários.
- Verificar a viabilidade da implementação.
- Estabelecer um modelo do sistema para ser construído posteriormente.

Se não fizermos isso adequadamente, podemos ter problemas sérios no futuro. Por exemplo, se o cliente pedir algo específico e os desenvolvedores não entenderem corretamente, pode ser uma perda de tempo e dinheiro considerável!

---

### **O que são Requisitos?**

Um requisito é basicamente uma condição ou capacidade que o sistema deve alcançar. Ele define claramente o que o software deve fazer.

Requisitos podem ser:

- **Funcionais**: O que o sistema DEVE fazer.
- **Não Funcionais**: Características do sistema, como desempenho, segurança e usabilidade.

### Níveis de requisitos

Nível de requisito varia:

- Declaração abstrata (alto nível) chamado requisito de usuário:
  - Linguagem natural (podendo ser apoiado por diagramas);
  - Quais serviços o sistema deverá fornecer a seus usuários;
  - Quais restrições com as quais o sistema deverá operar;
- Definição detalhada (baixo nível) chamado requisito de sistema:
  - Costuma ser chamado de "especificação de requisitos";
  - Deve definir exatamente o que deve ser implementado;
  - Pode ser parte do contrato entre comprador/desenvolvedores.

## **Requisitos Funcionais**

### **O que são?**

Requisitos funcionais definem as funcionalidades essenciais do sistema:

- São ações ou comportamentos que o software deve ter para atender às necessidades dos usuários.
- Declarações de serviços que o sistema deve fornecer.
- Declarações de como o sistema deve reagir a entradas específicas.
- Declarações de como o sistema deve se comportar em determinadas situações.
- Declarações do que o sistema não deve fazer.

**Exemplos:**

- RF01: O sistema deve permitir que os professores lancem notas e faltas dos alunos.
- RF02: O sistema deve emitir histórico escolar.
- RF03: O sistema deve calcular as notas médias das disciplinas.
- RF04: Deve ser possível emitir boletos para pagamento das mensalidades dos cursos.
- RF05: O sistema deve gerar nota fiscal.

### **Como identificar?**

Para identificar requisitos funcionais, precisamos conversar com o cliente ou usuários finais. Eles sabem exatamente o que querem e como querem que o software funcione.

---

## **Requisitos Não Funcionais**

### **O que são ?**

Requisitos não funcionais descrevem as características do sistema:

- como qualidade de desempenho, segurança ou usabilidade.
- Eles são mais amplos e abrangem aspectos que influenciam o funcionamento geral.
- Restrições aos serviços ou funções oferecidos pelo sistema.
- Incluem restrições de tempo, restrições no processo de desenvolvimento e restrições impostas por normas.
- Geralmente, aplicam-se ao sistema como um todo.

**Exemplos:**

- RNF01: O sistema deve ser rápido.
- RNF02: O sistema deve permitir impressão em PDF.
- RNF03: O sistema deve emitir relatórios toda sexta-feira.
- RNF04: O sistema deve ter boa segurança.
- RNF05: O sistema deve ser implementado usando a linguagem Python.
- RNF06: O acesso ao sistema não pode demorar mais do que 10 segundos;
- RNF07: Toda sexta-feira deverá ser emitido um relatório de faltas dos alunos;
- RNF08: Um aluno não poderá ter acesso aos dados dos outros alunos.

### **Classificação comum:**

Indicam características de qualidade que o sistema deve possuir e que estão relacionadas às funcionalidades previstas.

Algumas dessas características são:

- Desempenho
- Confiabilidade
- Escalabilidade
- Portabilidade
- Usabilidade
- Segurança

Requisitos não funcionais podem ser classificados como:

Requisitos do Produtos:

- Requisitos de usabilidade
- Requisitos de eficiência
- Requisitos de confiabilidade
- Requisitos de portabilidade

Requisitos Organizacionais:

- Requisitos de entrega
- Requisitos de implementação
- Requisitos de padrões.

Requisitos Externos:

- Requisitos de interoperabilidade
- Requisitos éticos
- Requisitos legais.

## **Técnicas para Levantar Requisitos**

Para obter os requisitos corretamente, usamos várias técnicas:

### Requisitos Funcionais

- Entrevistas com o cliente.
- Workshops (reuniões dinâmicas).
- Brainstorming.

### Requisitos Não Funcionais

- Questionários.
- Análise de casos de uso.
- Etnografia (observação do contexto).
- Workshops de requisitos
- Entrevistas com stakeholders
- Brainstorming
- Prototipagem
- Etnografia
- JAD (Joint Application Design)

É importante lembrar que, no levantamento de requisitos, NÃO colocamos soluções técnicas. Apenas definimos o escopo e as funcionalidades que o sistema deve ter.

### Requisitos Funcionais x Não-funcionais

| Requisitos Funcionais | Não-funcionais |
| --- | --- |
| Mandatórios | Não mandatórios |
| Visualizados em Casos de Uso | Atributos (Características) |
| Funcionalidade do Produto | Propriedades do Produto |
| Relativamente fáceis de descobrir | Mais difíceis de descobrir |
| Verbos | Restrições |
| Necessidades do negócio | Expectativas do negócio |

---

## **Documentação dos Requisitos**

Após coletarmos todos os requisitos, devemos documentá-los em um formato claro para todo mundo entender. Normalmente usamos:

- Texto formal.
- Casos de uso (método UML).
- Lista numerada com nomenclatura específica.

Isso ajuda a equipe técnica e o cliente a terem uma visão clara do que será desenvolvido!

---

### Atividades do Levantamento de Requisitos

Há três tipos de atividades realizadas no processo de levantamento de requisitos:

- Elicitação dos requisitos: Comunicação com os stakeholders (interessados) - para determinar quais são os requisitos de sistema.
- Análise de requisitos: determina o estado do requisitos (- inacabado, incompleto, ambíguo, contraditório) e resolver estes problemas.
- Registros dos requisitos: Documentar os requisitos de vária formas, como usando linguagem natural, casos de uso, ou ainda processo de especificação.

[Modelos gratuitos de requisitos de projetos - Smartsheet](https://pt.smartsheet.com/content/project-requirements-templates)

---

## Exemplo de sistema de gerenciamento de pacientes

>[!note] Definição de requisitos usuário:
> I. O MHC-PMS deve gerar relatórios gerenciais mensais que mostrem o custo dos medicamentos prescritos por cada clinica durante aquele mês.

>[!note] Especificação de requisitos de sistema
>
> - 1.1 No último dia útil de cada mês deve ser gerado um resumo dos medicamentos prescritos, seus custos e as prescrições de cada clinica.
> - 1.2 Após 17:30h do último dia útil do mês, o sistema deve gerar automaticamente o relatório para impressão.
> - 1.3 Um relatório será criado para cada clinica, listando os nomes dos medicamentos, o número total de prescrições, o número de doses prescritas e 0 custo total dos medicamentos prescritos.
> - 1.4 A Se os medicamentos estio disponíveis em diferentes unidades de dosagem (por exemplo, 10 mg, 20 mg), devem ser criados relatórios separados para cada unidade.
> - 1.5 0 acesso aos relatórios de custos deve ser restrito a usuários autorizados por uma lista de controle de gerenciamento de acesso.

---

>[!note] Requisitos Funcionais - sistema MHC-PMS:
>
> - Um usuário deve ser capaz de pesquisar as listas de agendamentos para todas as clínicas.
> - O sistema deve gerar a cada dia, para cada clínica, a lista dos pacientes para as consultas daquele dia.
> - Cada membro da equipe que usa o sistema deve ser identificado apenas por seu número de oito dígitos.

>[!note] Requisito nâo funcionais sistema MHC-PMS
> Requisito de produto:
>
> - O MHC-PMS deve estar disponível para todas as clinicas durante as horas normais de trabalho (segunda a sexta-feira, 8h30 às 17h30). Períodos de não operação dentro do horário normal de trabalho não podem exceder cinco segundos em um dia.
>
> Requisito organizacional:
>
> - Usuários do sistema MHC-PMS devem se autenticar com seus cartões de identificação da autoridade da saúde.
>
> Requisito externo:
>
> - O sistema deve implementar as disposições de privacidade dos pacientes, tal como estabelecido no HStan-03-2006-priv.

---

## **Bibliografia Recomendada**

Para entender melhor esse tema, recomendo os seguintes materiais:

- Bezerra, Eduardo. Princípios de Análise e Projeto de Sistemas com UML
- Somerville, l. Engenharia de software. 60 ed.
- Pressman, Roger S. - Engenharia de Software
- Medeiros, Higor. Introdução a Requisitos de Software. Disponível em: <https://www.devmedia.com.br/introducao-a-requisitos-de-software/29580>. Acesso em 05/09/2018
- Engholm Jr, Hélio. Engenharia de Software na Prática.

---

## **Conclusão**

Entender o que são os requisitos funcionais e não funcionais é fundamental no desenvolvimento de software. Eles nos ajudam a definir claramente o escopo do projeto e garantem que o sistema será construído conforme as necessidades reais.

Para saber mais assista: [O que é Levantamento de Requisitos - Tópicos de Engenharia de Software - YouTube](https://www.youtube.com/watch?v=VcOeM2AD8Yk), [Engenharia de Software - Aula 05 - Tipos de requisitos - YouTube](https://www.youtube.com/watch?v=Pn93e2fgIro)

[[Programador Web]]
