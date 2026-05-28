# ⚡ Fast Recon

> Scanner de portas TCP multi-threaded via CLI desenvolvido em Python para fins educacionais, aprendizado em networking e cybersecurity.

O **Fast Recon** é um projeto focado em reconhecimento de serviços de rede utilizando sockets TCP, multithreading e automação via terminal.  
O objetivo principal é praticar conceitos fundamentais de infraestrutura, redes e desenvolvimento de ferramentas CLI voltadas para cybersecurity.

---

# 🎯 Objetivo

Este projeto foi desenvolvido para praticar e consolidar conhecimentos em:

- Python
- Networking
- Multithreading
- Reconhecimento de serviços
- Aplicações CLI
- Cybersecurity

Além disso, o projeto busca melhorar habilidades relacionadas à arquitetura modular, manipulação de sockets e automação de tarefas de rede.

---

# 🚀 Funcionalidades

- ✅ Validação de IP e hostname
- ✅ Resolução DNS automática
- ✅ TCP Port Scanning
- ✅ Multithreading configurável
- ✅ Banner Grabbing
- ✅ Identificação de serviços comuns
- ✅ Medição de tempo de execução
- ✅ Registro de horário de início e término da varredura

---

# 🛠️ Tecnologias Utilizadas

O projeto utiliza apenas bibliotecas nativas do Python:

- `Python 3`
- `socket`
- `concurrent.futures`
- `ThreadPoolExecutor`
- `sys`
- `datetime`
- `ipaddress`

---

# ▶️ Estrutura de Execução

```bash
python3 main.py hostname portainicio portafinal threads(opcional)
```

### Exemplo:

```bash
python3 main.py scanme.nmap.org 1 1000 250
```

### Parâmetros:

| Argumento | Descrição |
|---|---|
| `hostname/IP` | Alvo da varredura |
| `porta inicial` | Porta inicial do scan |
| `porta final` | Porta final do scan |
| `threads` | Quantidade de threads utilizadas (opcional) |

---

# ⚙️ Sistema de Threads

O Fast Recon utiliza **multithreading** para aumentar significativamente a velocidade da varredura.

### Limites configurados:

- 🔹 Mínimo: `150 threads`
- 🔹 Máximo: `400 threads`

O uso de múltiplas threads permite executar diversas conexões simultaneamente, reduzindo o tempo total do scan e melhorando a performance da aplicação.

---

# 🖥️ Exemplo de Saída

```bash
==================================================
            FAST RECON - TCP SCANNER
==================================================

[+] Hostname: scanme.nmap.org
[+] IP Resolvido: 45.33.32.156
[+] Porta 22  -> OpenSSH 6.6.1
[+] Porta 80  -> HTTP
[+] Porta 443 -> HTTPS

--------------------------------------------------

[+] Horário de início : 20:14:03
[+] Horário de término: 20:14:08
[+] Tempo total       : 5 segundos

==================================================
```

---

# 📁 Estrutura do Projeto

```bash
fast-recon/
│
├── main.py
├── module/
│   ├── dns.py
│   ├── portscan.py
│   └── banner.py
│
├── utils/
│   └── validator.py
│
└── README.md
```

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conhecimentos relacionados a:

- Programação com sockets
- Concorrência e multithreading
- Arquitetura modular
- Validação de entrada de usuários
- DNS e networking
- Aplicações CLI
- Reconhecimento de serviços de rede

O projeto também contribui para o entendimento prático de como scanners de rede funcionam internamente.

---

# 🗺️ Roadmap / Futuras Melhorias

Ideias futuras para evolução do projeto:

- [ ] Exportação JSON
- [ ] Exportação CSV
- [ ] Melhor detecção de serviços
- [ ] UDP Scan
- [ ] Sistema de Logging
- [ ] Configuração via arquivo
- [ ] Melhor tratamento de erros
- [ ] Timeout configurável
- [ ] Suporte a IPv6

---

# ⚠️ Aviso Ético

Este projeto foi desenvolvido exclusivamente para fins educacionais e de aprendizado em cybersecurity.

- Os testes devem ser realizados apenas em ambientes autorizados.
- Não utilize a ferramenta contra sistemas sem permissão.
- O uso inadequado da aplicação é de total responsabilidade do usuário.

---

# 📦 Requisitos

## Instalação

```bash
# Clonar repositório
git clone https://github.com/seuusuario/fast-recon.git

# Entrar na pasta
cd fast-recon

# Executar aplicação
python3 main.py scanme.nmap.org 1 1000 250
```

## Requisitos mínimos

- Python 3 instalado
- Terminal Linux/Windows/macOS
- Conhecimentos básicos em redes e CLI

---

# 👨‍💻 Considerações Finais

O Fast Recon é um projeto voltado para evolução prática em Python, networking e cybersecurity, focando principalmente no entendimento de sockets, concorrência e automação de tarefas de reconhecimento de rede.

Esse projeto representa uma etapa importante no desenvolvimento de habilidades voltadas para segurança ofensiva, engenharia de software e infraestrutura de redes.