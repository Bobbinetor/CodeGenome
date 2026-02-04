# CodeGenome - Guida Sperimentale con run_experiment.py

![CodeGenome Suite](cli.png)

**Generazione di Varianti Binarie tramite LLM e Metamorfismo**

> ⚠️ **NOTA IMPORTANTE**
>
> Questa guida si concentra esclusivamente su **`run_experiment.py`**, una versione semplificata e sperimentale di CodeGenome. Questo script è pensato per esplorare la generazione di varianti binarie funzionalmente equivalenti tramite LLM e confrontarle con tool tradizionali come MetaME.

---

## 📚 Indice

- [Cos'è questo Progetto](#-cosè-questo-progetto)
- [Prerequisiti e Installazione](#-prerequisiti-e-installazione)
- [Comprendere il Workflow](#-comprendere-il-workflow)
- [Guida Rapida](#-guida-rapida)
- [Parametri di Configurazione](#-parametri-di-configurazione)
- [Il Processo di Patching](#-il-processo-di-patching)
- [Test di Equivalenza](#-test-di-equivalenza)
- [Metriche e Analisi](#-metriche-e-analisi)
- [Risoluzione Problemi](#-risoluzione-problemi)

---

## 🎯 Cos'è questo Progetto

### Obiettivo
Generare **varianti binarie** di un programma che siano:
1. **Strutturalmente diverse** - Il codice macchina è differente
2. **Funzionalmente equivalenti** - Producono lo stesso output

### Il Problema del Patching

> ⚠️ **STATO ATTUALE: WORK IN PROGRESS**
>
> Le patch generate dall'LLM **NON funzionano sempre**. L'obiettivo di questo progetto sperimentale è trovare il modo corretto di patchare il binario affinché:
> - La patch venga applicata con successo
> - Il binario compili correttamente  
> - Il binario rimanga funzionalmente equivalente all'originale
>
> Questo README documenta lo stato attuale e il workflow per sperimentare.

### Perché run_experiment.py?
`run_experiment.py` è uno script standalone che permette di:
- Configurare l'esperimento modificando variabili in cima al file
- Generare varianti con MetaME (baseline tradizionale)
- Generare varianti con LLM (sperimentale)
- Confrontare i risultati

---

## 🛠️ Prerequisiti e Installazione

### 1. Requisiti di Sistema

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install build-essential gcc git python3 python3-pip
```

### 2. Dipendenze Python

```bash
pip install -r requirements.txt
```

Le dipendenze principali sono:
- `rich` - Interfaccia terminale
- `requests` - Chiamate HTTP alle API
- `keystone-engine` - Assemblaggio istruzioni

---

### 3. Installazione MetaME (Baseline)

MetaME è un motore metamorfico tradizionale che useremo come baseline di confronto.

#### 3.1 Prerequisiti per radare2

```bash
# Supporto architettura 32-bit
sudo dpkg --add-architecture i386
sudo apt update

# Tool di sviluppo
sudo apt install build-essential git
sudo apt install libc6-dev-i386 gcc-multilib g++-multilib
```

#### 3.2 Installare radare2 (versione specifica!)

> ⚠️ MetaME richiede una versione specifica di radare2

```bash
git clone https://github.com/radareorg/radare2.git
cd radare2
git checkout 41dc7e6db6932ebca90a9bc66ee58ee845880fee
sudo sys/install.sh
cd ..
```

#### 3.3 Installare MetaME

```bash
pip install metame
```

Verifica l'installazione:
```bash
metame --help
```

---

### 4. Configurazione Ollama Cloud

Per usare modelli LLM performanti tramite Ollama Cloud:

#### 4.1 Installare Ollama

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### 4.2 Creare Account e API Key

1. Vai su [ollama.com](https://ollama.com)
2. Crea un account
3. Vai nelle impostazioni e genera una **API Key**

#### 4.3 Autenticazione

```bash
ollama signin
# Inserisci la tua API key quando richiesto
```

#### 4.4 Modelli Consigliati

Dopo il signin, puoi usare modelli cloud performanti, li puoi trovare su internet vendo ollama models, sono contraddistinti dalla dicitura cloud, per esempio:
- gpt-oss:120b-cloud

---

### 5. Alternativa: OpenRouter (API OpenAI-compatibile)

Se preferisci usare API OpenAI-compatibili con accesso a più modelli:

#### 5.1 Creare Account OpenRouter

1. Vai su [openrouter.ai](https://openrouter.ai)
2. Crea un account
3. **Carica credito** nel tuo wallet (richiesto per usare i modelli)
4. Copia la tua API key

#### 5.2 Configurazione nello Script

Modifica `run_experiment.py`:

```python
OLLAMA_BASE_URL = "https://openrouter.ai/api/v1"
# Aggiungi header autorizzazione nelle chiamate
```

> 📝 Vedi sezione [Parametri di Configurazione](#-parametri-di-configurazione) per dettagli.

---

## 🔄 Comprendere il Workflow

### Flusso di Esecuzione

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT                                     │
│  source_code/calcolatrice.c                                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  COMPILAZIONE                                │
│  gcc → calcolatrice_original (binario ELF)                  │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
┌───────────────────┐                 ┌───────────────────┐
│    METAME         │                 │    LLM            │
│    (Baseline)     │                 │    (Sperimentale) │
│                   │                 │                   │
│  Trasformazioni   │                 │  1. Disassembla   │
│  a livello byte:  │                 │  2. LLM genera    │
│  - NOP insertion  │                 │     patch ASM     │
│  - Jmp subst.     │                 │  3. Applica patch │
│  - Reg. rename    │                 │  4. Verifica      │
└───────────────────┘                 └───────────────────┘
        │                                       │
        └───────────────────┬───────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  VARIANTI GENERATE                           │
│  calcolatrice_metame_v01, calcolatrice_gemma3_v01, ...     │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  TEST EQUIVALENZA                            │
│  Esegui ogni variante con stessi input                      │
│  Confronta output con originale                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  ANALISI E METRICHE                          │
│  - Distanza Euclidea/Coseno                                 │
│  - Radar charts                                             │
│  - Report CSV/JSON                                          │
└─────────────────────────────────────────────────────────────┘
```

### Le Due Modalità

| Modalità | Descrizione |
|----------|-------------|
| `binary` | Disassembla il binario e genera patch ASM con LLM |
| `source` | Trasforma il codice C sorgente con LLM |

Per questo lavoro useremo principalmente la modalità **binary**.

---

## 🚀 Guida Rapida

### Passo 1: Configura lo Script

Apri `run_experiment.py` e modifica le variabili di configurazione (linee 21-74):

```python
# File sorgente C da usare
SOURCE_FILE = "source_code/calcolatrice.c"

# Modalità: "source" o "binary"
EXPERIMENT_MODE = "binary"

# Abilita/disabilita strumenti
USE_METAME = True      # Generare varianti MetaME?
USE_LLM = True         # Generare varianti LLM?

# Configurazione LLM
OLLAMA_MODEL = "gemma3:12b"
LLM_MODELS = [
    {"model": "gemma3:12b", "variants": 2},
]
```

### Passo 2: Esegui Solo MetaME (Test Iniziale)

Per verificare che l'installazione funzioni, inizia solo con MetaME:

```python
USE_METAME = True
USE_LLM = False        # Disabilita LLM per ora
METAME_NUM_VARIANTS = 2
```

Esegui:
```bash
python3 run_experiment.py
```

### Passo 3: Esegui con LLM

Una volta verificato MetaME, abilita l'LLM:

```python
USE_METAME = True
USE_LLM = True
LLM_MODELS = [
    {"model": "gemma3:12b", "variants": 2},
]
```

Esegui:
```bash
python3 run_experiment.py
```

### Output

I risultati vengono salvati in:
```
workspace/experiments/exp_YYYYMMDD_HHMMSS/
├── calcolatrice_original          # Binario originale
├── calcolatrice_metame_v01        # Variante MetaME 1
├── calcolatrice_metame_v02        # Variante MetaME 2
├── calcolatrice_gemma3_v01        # Variante LLM 1
├── calcolatrice_gemma3_v01.asm    # ASM delle patch
├── original.asm                   # Disassemblato originale
├── raw_llm_io.txt                 # Log I/O con LLM
├── results_complete.csv           # Report risultati
└── analysis_results/              # Analisi comparative
    ├── radar_comparison.png
    └── advanced_analysis_report.json
```

---

## ⚙️ Parametri di Configurazione

### Configurazione Base (linee 21-50)

| Parametro | Valore Default | Descrizione |
|-----------|----------------|-------------|
| `SOURCE_FILE` | `"source_code/calcolatrice.c"` | File C sorgente |
| `EXPERIMENT_MODE` | `"binary"` | `"source"` o `"binary"` |
| `EXPERIMENT_NAME` | auto-generato | Nome cartella output |
| `WORKSPACE_DIR` | `"workspace/experiments"` | Directory output |

### Configurazione LLM (linee 32-51)

| Parametro | Valore Default | Descrizione |
|-----------|----------------|-------------|
| `USE_LLM` | `True` | Abilita generazione LLM |
| `LLM_TIMEOUT` | `300` | Timeout in secondi |
| `LLM_TEMPERATURE` | `0.4` | Creatività (0.0-1.0) |
| `OLLAMA_BASE_URL` | `"http://localhost:11434"` | URL API Ollama |
| `OLLAMA_MODEL` | `"gemma3:12b"` | Modello default |
| `LLM_MODELS` | Lista | Configurazione multi-modello |

### Configurazione Patching (linee 47-51)

| Parametro | Valore Default | Descrizione |
|-----------|----------------|-------------|
| `DISASSEMBLER` | `"objdump"` | `"objdump"` o `"radare2"` |
| `ASM_SYNTAX` | `"intel"` | `"intel"` o `"att"` |
| `REASSEMBLY_METHOD` | `"r2patch"` | `"r2patch"`, `"keystone"`, `"gas_full"` |
| `PATCH_STRATEGY` | `"multi_strategy"` | `"function_rewrite"` o `"multi_strategy"` |

### Configurazione MetaME (linee 53-57)

| Parametro | Valore Default | Descrizione |
|-----------|----------------|-------------|
| `USE_METAME` | `True` | Abilita MetaME |
| `METAME_PATH` | path assoluto | Percorso eseguibile metame |
| `METAME_NUM_VARIANTS` | `2` | Numero varianti da generare |

---

## 🔧 Il Processo di Patching

### Cos'è il Patching Binario

Il **patching binario** consiste nel modificare direttamente le istruzioni macchina in un eseguibile compilato, senza ricompilare da sorgente.

Esempio:
```
Originale:  xor eax, eax    (2 bytes: 31 C0)
Patch:      sub eax, eax    (2 bytes: 29 C0)
```

Entrambe le istruzioni azzerano il registro `eax`, ma hanno encoding diverso.

### Le 6 Strategie di Trasformazione

Lo script usa `multi_aspect_llm_transform.py` che implementa 6 strategie:

| # | Strategia | Descrizione |
|---|-----------|-------------|
| 1 | **Function** | Riscrive intere funzioni |
| 2 | **Basic Block** | Trasforma blocchi di istruzioni |
| 3 | **CFG** | Modifica salti condizionali (je↔jz) |
| 4 | **Data** | Trasforma riferimenti a dati |
| 5 | **Call** | Modifica chiamate di funzione |
| 6 | **Stack** | Trasforma operazioni stack |

### Vincoli di Dimensione

> ⚠️ **REGOLA FONDAMENTALE**: La nuova istruzione deve avere dimensione **≤** all'originale

Perché? Il binario ha indirizzi fissi. Se inseriamo un'istruzione più grande, "schiacciamo" quella successiva.

```
VIETATO:
  mov eax, 0      (5 bytes)  →  push rbx; xor ebx,ebx; mov eax,ebx; pop rbx  (10+ bytes)
                                 ^^^^^^^^ NON ENTRA! ^^^^^^^^

PERMESSO:
  mov eax, 0      (5 bytes)  →  xor eax, eax  (2 bytes) + NOP padding (3 bytes)
                                 ^^^^^^^^ OK, più piccolo ^^^^^^^^
```

### Verifica Per-Patch con Rollback

Per ogni patch proposta dall'LLM, lo script:

1. **Salva** i bytes originali
2. **Applica** la patch
3. **Testa** il binario con input di prova
4. **Se funziona**: mantiene la patch
5. **Se fallisce**: **rollback** ai bytes originali

```python
# Pseudocodice del processo
for patch in patches:
    original_bytes = read(file, patch.address)
    write(file, patch.address, patch.new_bytes)
    
    if test_binary() == FAIL:
        write(file, patch.address, original_bytes)  # Rollback!
        log("Patch annullata")
    else:
        log("Patch applicata")
```

### ⚠️ Attenzione al "Cheating" dell'LLM

> **IMPORTANTE**: L'LLM potrebbe iniziare a "barare"!

Quando si usa vibe coding o agent-based coding, l'LLM potrebbe:
- Inserire **patch hardcoded** invece di trasformazioni genuine
- Proporre soluzioni **non generalizzabili**
- "Memorizzare" pattern specifici invece di capire il problema

**Come verificare**:
- Controlla il file `raw_llm_io.txt` per vedere le patch proposte
- Assicurati che le trasformazioni siano semanticamente equivalenti
- Prova con programmi diversi per verificare la generalizzazione

---

## ✅ Test di Equivalenza

### Cos'è l'Equivalenza Funzionale

Due binari sono **funzionalmente equivalenti** se:
- Dati gli **stessi input**, producono gli **stessi output**

### Generazione Automatica Test Cases

Lo script chiede all'LLM di generare test cases analizzando il codice sorgente:

```python
# Esempio output LLM
[
    {"input": "5\n3\n+\n", "description": "Test addizione 5+3"},
    {"input": "10\n2\n/\n", "description": "Test divisione 10/2"},
    {"input": "0\n", "description": "Test input zero"}
]
```

### Processo di Validazione

1. Esegui **binario originale** con ogni test case → salva output
2. Esegui **variante** con stessi input → confronta output
3. Se tutti i test passano → variante **equivalente**

### Output nel Terminale

```
🧪 Running equivalence tests on gemma3_V1...
  ✅ Test addizione 5+3: PASS
  ✅ Test divisione 10/2: PASS
  ❌ Test input zero: FAIL
     Expected: "Risultato: 0"
     Got: "Errore: divisione per zero"
⚠️ gemma3_V1: 2/3 tests passed
```

---

## 📊 Metriche e Analisi

### Distanza Euclidea

Misura la **differenza numerica** tra feature vectors dei binari.

```
Distanza = √[(a₁-b₁)² + (a₂-b₂)² + ... + (aₙ-bₙ)²]
```

- **0** = binari identici
- **Più alta** = binari più diversi

### Distanza Coseno

Misura la **differenza direzionale** tra feature vectors (ignora la magnitudine).

```
Distanza = 1 - (A·B) / (|A|×|B|)
```

- **0** = stessa direzione (simili)
- **1** = ortogonali (molto diversi)

### Radar Charts

I radar chart mostrano visivamente come le varianti differiscono dall'originale su più metriche:

- **Dimensione binario**
- **Numero funzioni**
- **Entropia**
- **Complessità ciclomatica**
- ecc.

### Confronto LLM vs MetaME

L'obiettivo finale è confrontare:

| Metrica | MetaME | LLM |
|---------|--------|-----|
| Tasso successo patch | ~100% | Da verificare |
| Diversità binario | Media | Potenzialmente alta |
| Equivalenza funzionale | Alta | Da verificare |

---

## 🔧 Risoluzione Problemi

### "Ollama connection failed"

```bash
# Verifica che Ollama sia in esecuzione
ollama serve &

# Verifica autenticazione
ollama signin
```

### "MetaME not found"

```bash
# Verifica installazione
which metame
pip show metame

# Aggiorna il path in run_experiment.py
METAME_PATH = "/path/to/your/metame"
```

### "Keystone assembly failed"

L'istruzione generata dall'LLM non è valida. Possibili cause:
- Istruzione non supportata (es. `endbr64`)
- Sintassi errata
- Riferimenti a simboli non risolti

### "No patches applied"

L'LLM non ha generato patch valide. Prova:
- Aumentare `LLM_TEMPERATURE` (più creatività)
- Usare un modello più grande
- Verificare che il binario abbia funzioni patchabili

### Patch applicate ma binario non funziona

Il meccanismo di rollback dovrebbe prevenire questo, ma se succede:
- Controlla `raw_llm_io.txt` per vedere le patch
- Prova con `USE_METAME=True, USE_LLM=False` per verificare il baseline

---

## 📜 Licenza

Questo progetto è sotto licenza MIT - vedi file `LICENSE`.

---

**CodeGenome - run_experiment.py** - Script sperimentale per la ricerca sulla generazione di varianti binarie tramite LLM.
