# PyBlueSniff

**PyBlueSniff** é um sniffer Bluetooth baseado em linha de comando, inspirado na simplicidade de uso do `nmap`. Ele permite capturar e filtrar pacotes Bluetooth utilizando a ferramenta `hcidump` no Linux.

> ⚠️ Este script requer permissões de superusuário (sudo) e funciona apenas em sistemas baseados em Linux.

---

## 🚀 Requisitos

- Python 3.x
- Linux com suporte a Bluetooth
- Ferramentas instaladas:
  - `bluez`
  - `hcitool`
  - `hcidump`

Instale com:

```bash
sudo apt update
sudo apt install bluez
```

---

## 🔧 Instalação

Clone o repositório ou salve o script `pybluesniff.py` em seu sistema.

---

## 💻 Uso

```bash
sudo python3 pybluesniff.py [opções]
```

### 🧩 Opções

| Opção           | Descrição                                                     |
|----------------|----------------------------------------------------------------|
| `--filter`      | Endereço MAC para aplicar um filtro (ex: `00:11:22:33:44:55`) |
| `--outfile`     | Nome do arquivo de saída (padrão: `bluesniff_log.txt`)       |
| `--interface`   | Interface Bluetooth a ser usada (ex: `hci0`, `hci1`)          |
| `--help`        | Exibe o manual de uso                                         |

---

### 📦 Exemplos

Capturar todos os pacotes Bluetooth:

```bash
sudo python3 pybluesniff.py
```

Capturar pacotes apenas de um dispositivo específico:

```bash
sudo python3 pybluesniff.py --filter 00:11:22:33:44:55
```

Salvar a saída em um arquivo personalizado:

```bash
sudo python3 pybluesniff.py --outfile captura_bt.log
```

Usar uma interface específica:

```bash
sudo python3 pybluesniff.py --interface hci1
```

---

## 📄 Exemplo de Saída

```
[+] Iniciando captura com interface hci0
[+] Log: bluesniff_log.txt
[+] Filtro MAC ativo: 00:11:22:33:44:55
[*] Capturando pacotes... pressione Ctrl+C para parar.

[2025-05-14 10:43:12] > ACL data: handle 11 flags 0x02 dlen 12
[2025-05-14 10:43:12] > L2CAP(d): cid 0x0040 len 8 [psm 3]
```

---

## 📘 Licença

Distribuído sob a licença MIT. Livre para uso e modificação.

---

## 🤝 Créditos

Script inspirado em ferramentas como [`bluesniff`](https://tools.kali.org/wireless-attacks/bluesniff) e `nmap`. Desenvolvido para fins educacionais e de análise de tráfego Bluetooth.
