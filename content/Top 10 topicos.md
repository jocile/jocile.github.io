---
title: 🔝 Top 10 tópicos
description: Os 10 tópicos com mais notas
tags:
  -
---

## Top 10 [Tópicos](/tags/)

<!-- QueryToSerialize: 
TABLE WITHOUT ID elink("tags/" + replace(string(t), "#", ""), replace(string(t), "#", "")) as "Tópicos",
count AS "Contagem" 
WHERE !draft
AND !contains(file.folder,"gemini-scribe")
AND !contains(file.folder,"private")
AND !contains(file.name,"index")
FLATTEN tags AS t 
GROUP BY t 
FLATTEN length(rows.file.link) as count 
SORT count DESC, t ASC
LIMIT 10 -->
<!-- SerializedQuery: TABLE WITHOUT ID elink("tags/" + replace(string(t), "#", ""), replace(string(t), "#", "")) as "Tópicos", count AS "Contagem" WHERE !draft AND !contains(file.folder,"gemini-scribe") AND !contains(file.folder,"private") AND !contains(file.name,"index") FLATTEN tags AS t GROUP BY t FLATTEN length(rows.file.link) as count SORT count DESC, t ASC LIMIT 10 -->

| Tópicos                                                                         | Contagem |
| ------------------------------------------------------------------------------- | -------- |
| [Teologia/Escatologia](tags/Teologia/Escatologia)                               | 31       |
| [Inteligencia-artificial/Ferramentas](tags/Inteligencia-artificial/Ferramentas) | 27       |
| [Formação](tags/Formação)                                                       | 26       |
| [excalidraw](tags/excalidraw)                                                   | 23       |
| [Inteligencia-artificial](tags/Inteligencia-artificial)                         | 22       |
| [Teologia/tipologia](tags/Teologia/tipologia)                                   | 22       |
| [Bíblia/Apocalipse](tags/Bíblia/Apocalipse)                                     | 19       |
| [Teologia/Cristologia](tags/Teologia/Cristologia)                               | 19       |
| [diagrama](tags/diagrama)                                                       | 18       |
| [Webdesign](tags/Webdesign)                                                     | 18       |

<!-- SerializedQuery END -->
