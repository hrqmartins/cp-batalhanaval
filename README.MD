# ⚓ SEIGUN - BATALHA NAVAL 🚢

![Battleship GIF](https://media.tenor.com/2vQnQ2rQGzMAAAAC/battleship.gif)
*Fluxograma do funcionamento do jogo (arquivo disponível na pasta `docs`).*

---

## 📝 Descrição do Projeto

O **SEIGUN** é um projeto desenvolvido como parte do **checkpoint da FIAP**, criado para simular o clássico jogo **Batalha Naval** no terminal.  

O jogo permite que o usuário tente acertar navios escondidos em um tabuleiro 5x5, com regras simples e interface de texto.  

### Funcionalidades principais

- Criação e visualização do tabuleiro  
- Posicionamento aleatório de navios  
- Sistema de ataque com feedback para acertos e erros  
- Controle de tentativas e finalização do jogo  
- Menu interativo com opções de jogar, instruções e sair  

---

## 📂 Estrutura de Pastas

```
CP-BATALHANAVAL/
│
├── docs/
│ ├── fluxograma.png
│ └── documentacao_codigo
│
└── batalhanaval.py
```

---

## 🎮 Como Jogar

1. Execute o programa no terminal:
``
python batalhanaval.py
``

2. Escolha uma das opções do menu:

- `1️⃣` - Iniciar Batalha  
- `2️⃣` - Como Funciona?  
- `3️⃣` - Sair  

1. No modo batalha:

- Escolha a linha e a coluna para atacar  
- O tabuleiro será atualizado após cada ataque  
- Objetivo: acertar todos os 3 navios escondidos  

---

## ⚙️ Funcionalidades Detalhadas

1. **Menu principal interativo**  
   Permite ao usuário iniciar o jogo, visualizar instruções ou sair  

2. **Criação do tabuleiro**  
   Um tabuleiro 5x5 é criado dinamicamente para cada partida  

3. **Posicionamento aleatório de navios**  
   O jogo posiciona 3 navios aleatoriamente sem revelar suas posições  

4. **Sistema de ataque**  
   - `X` → Acerto de navio  
   - `O` → Água  
   - Repetição de ataque → aviso ao jogador  

5. **Contagem de tentativas**  
   O jogador recebe feedback do número de tentativas até acertar todos os navios  

6. **Instruções de jogo**  
   Um menu explicativo mostra as regras e dicas de estratégia  

---

## 💻 Tecnologias Utilizadas

- **Python 3.x**  
- Bibliotecas padrão: `random`, `os`  

---

## 👥 Equipe

- **Henrique Martins** – RM563620  
- **Henrique Texeira** – RM563088  

---

## 📚 Documentação e Fluxograma

- **`docs/documentacao_codigo.md`** → Explica a lógica do código, funções e fluxo do jogo  
- **`docs/fluxograma.png`** → Representa visualmente o fluxo do jogo  

---

## ⚠️ Observações

- O programa foi desenvolvido para rodar em terminal/console  
- Compatível com Windows, Linux e macOS (usa `os.system` para limpar o terminal)  
- Projeto criado com foco acadêmico para checkpoint da FIAP  

---

🎯 **Divirta-se e boa sorte no jogo!**
